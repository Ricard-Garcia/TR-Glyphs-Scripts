# MenuTitle: Quadrant mover (UI)
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

import math
import random

from AppKit import NSColor
from GlyphsApp import *
from vanilla import *

Glyphs.clearLog()


def _rect_center(rect):
	return rect.origin.x + rect.size.width * 0.5, rect.origin.y + rect.size.height * 0.5


def _rotation_matrix_around(cx, cy, angle_degrees):
	rad = math.radians(angle_degrees)
	cos_t = math.cos(rad)
	sin_t = math.sin(rad)
	tx = cx - cos_t * cx + sin_t * cy
	ty = cy - sin_t * cx - cos_t * cy
	# GlyphsApp path.applyTransform uses the CoreGraphics/CGAffineTransform
	# convention: [a, b, c, d, tx, ty] where
	#   x' = a*x + c*y + tx
	#   y' = b*x + d*y + ty
	# For a rotation by +angle:
	#   a=cos, b=sin, c=-sin, d=cos
	return [cos_t, sin_t, -sin_t, cos_t, tx, ty]


def _radial_vector(px, py, gx, gy, distance):
	"""
	Returns a normalized vector from glyph center → path center,
	scaled by distance (centrifugal movement).
	"""
	dx = px - gx
	dy = py - gy

	length = math.hypot(dx, dy)

	# If path is exactly at center, choose random direction
	if length == 0:
		angle = random.uniform(0, 2 * math.pi)
		return math.cos(angle) * distance, math.sin(angle) * distance

	# Normalize
	nx = dx / length
	ny = dy / length

	return nx * distance, ny * distance


def _parse_float_field(s, label):
	try:
		return float(s.strip().replace(",", "."))
	except:
		Message("Quadrant mover", "Invalid number for %s." % label, OKButton=None)
		return None


def _try_parse_float(s):
	try:
		return float(s.strip().replace(",", "."))
	except Exception:
		return None


def _format_range_error_message(bad):
	if len(bad) == 2:
		return "Min cannot be more than max for angle and distance."
	return "Min cannot be more than max for %s." % bad[0]


class QuadrantMover(object):

	def __init__(self):
		self.f = Glyphs.font
		if self.f is None:
			Message("Quadrant mover", "No font open.", OKButton=None)
			return

		margin = 12
		line = 12
		row_h = 18
		w = 300
		status_h = 40
		h = margin * 2 + row_h * 4 + status_h + 8

		self.w = FloatingWindow((w, h), "Quadrant mover")
		y = margin

		self.w.angleLabel = TextBox((margin, y, 130, row_h), "Angle min / max (°):", sizeStyle="small")
		self.w.angleMin = EditText((140, y - 2, 68, 20), "0", sizeStyle="small", callback=self._on_range_edited)
		self.w.angleMax = EditText((215, y - 2, 68, 20), "25", sizeStyle="small", callback=self._on_range_edited)
		y += row_h + line

		self.w.distLabel = TextBox((margin, y, 130, row_h), "Distance min / max:", sizeStyle="small")
		self.w.distMin = EditText((140, y - 2, 68, 20), "20", sizeStyle="small", callback=self._on_range_edited)
		self.w.distMax = EditText((215, y - 2, 68, 20), "80", sizeStyle="small", callback=self._on_range_edited)
		y += row_h + line + 4
		self.w.statusLine = TextBox((margin, y, -margin, status_h), "", sizeStyle="small")
		y += 24 + 6

		self.w.applyButton = Button((margin, y, -margin, 24), "Apply to selected layers", callback=self.applyCallback)

		self.w.open()

	def _set_status_error(self, message):
		text = u"\u2717 " + message
		self.w.statusLine.set(text)
		self.w.statusLine._nsObject.setTextColor_(NSColor.redColor())

	def _clear_status(self):
		self.w.statusLine.set("")
		self.w.statusLine._nsObject.setTextColor_(NSColor.secondaryLabelColor())

	def _on_range_edited(self, sender):
		self._update_range_status()

	def _update_range_status(self):
		a0 = _try_parse_float(self.w.angleMin.get())
		a1 = _try_parse_float(self.w.angleMax.get())
		d0 = _try_parse_float(self.w.distMin.get())
		d1 = _try_parse_float(self.w.distMax.get())
		bad = []
		if a0 is not None and a1 is not None and a0 > a1:
			bad.append("angle")
		if d0 is not None and d1 is not None and d0 > d1:
			bad.append("distance")
		if bad:
			self._set_status_error(_format_range_error_message(bad))
		else:
			self._clear_status()

	def applyCallback(self, sender):
		f = Glyphs.font
		if f is None:
			return

		a0 = _parse_float_field(self.w.angleMin.get(), "angle min")
		a1 = _parse_float_field(self.w.angleMax.get(), "angle max")
		d0 = _parse_float_field(self.w.distMin.get(), "distance min")
		d1 = _parse_float_field(self.w.distMax.get(), "distance max")

		if None in (a0, a1, d0, d1):
			return

		bad = []
		if a0 > a1:
			bad.append("angle")
		if d0 > d1:
			bad.append("distance")
		if bad:
			self._set_status_error(_format_range_error_message(bad))
			return

		self._clear_status()
		amin, amax = a0, a1
		dmin, dmax = d0, d1

		selected_layers = f.selectedLayers
		if not selected_layers:
			Message("Quadrant mover", "No layer selected.", OKButton=None)
			return

		count = 0

		for layer in selected_layers:
			gx, gy = _rect_center(layer.bounds)

			for path in layer.paths:
				pb = path.bounds
				if pb.size.width <= 0 and pb.size.height <= 0:
					continue

				px, py = _rect_center(pb)

				# RANDOMS
				angle = random.uniform(amin, amax)
				dist = random.uniform(dmin, dmax)

				# TRUE RADIAL MOVEMENT
				sx, sy = _radial_vector(px, py, gx, gy, dist)

				# APPLY TRANSFORMS
				# Translate first, then rotate around the path's *new* center.
				# (Translation moves the center by (sx, sy).)
				path.applyTransform([1.0, 0.0, 0.0, 1.0, sx, sy])
				path.applyTransform(_rotation_matrix_around(px + sx, py + sy, angle))

				count += 1

		if count == 0:
			Message("Quadrant mover", "No paths on the selected layer(s).", OKButton=None)
		else:
			print("Quadrant mover: transformed %s path(s)." % count)


QuadrantMover()

print("Done!")