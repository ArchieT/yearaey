# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chkrng:
	def __init__(self,sy,ey):
		if not (isinstance(sy,int) and isinstance(ey,int)):
			raise ValueError
	def checkem(self):
		self.sy = sy
		self.ey = ey
		fs = "{0:b}"
		bulijan = {}

		from ownlib.chksngl import chksngl
		for i in range(sy,ey+1):
			print i
			c = chksngl(i)
			bulijan[i] = c.isit()