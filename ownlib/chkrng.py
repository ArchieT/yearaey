# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chkrng:
	def __init__(self,sy,ey):
		if not (isinstance(sy,int) and isinstance(ey,int)):
			raise ValueError
		else:
			self.sy = sy
			self.ey = ey
	def checkem(self,pt=True,pf=False,wsl=14):
		sy = self.sy
		ey = self.ey

		bulijan = {}

		from ownlib.chksngl import chksngl
		for i in range(sy,ey+1):
			#print i
			c = chksngl(i)
			b = c.isit
			bulijan[i] = b
			if pt and b: c.printsingle(wsl)
			if pf and not b: c.printsingle(wsl)
			#print c.polowyjoined, b, c.plwni

		self.bulijan = bulijan

	@property
	def outbulijan(self):
		return self.bulijan