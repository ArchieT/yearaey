# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chkrng:
	def __init__(self,sy,ey):
		if not (isinstance(sy,int) and isinstance(ey,int)):
			raise ValueError
		else:
			self.sy = sy
			self.ey = ey
	def checkem(self):
		sy = self.sy
		ey = self.ey

		bulijan = {}

		from ownlib.chksngl import chksngl
		for i in range(sy,ey+1):
			print i
			c = chksngl(i)
			b = c.isit()
			bulijan[i] = b
			print c.polowy(), b, c.plwni

		self.bulijan = bulijan

	def outbulijan(self):
		return self.bulijan