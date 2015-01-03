# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chkrng:
	def __init__(self,sy,ey):
		if not (isinstance(sy,int) and isinstance(ey,int)):
			raise ValueError
		else:
			self.sy = sy
			self.ey = ey
	def checkem(self,pt=True,pf=False,db=False,sposob='bruteforcebyreversing',wsl=14):
		sy = self.sy
		ey = self.ey

		bulijan = {}

		from ownlib.chksngl import chksngl
		for i in range(sy,ey+1):
			#print i
			c = chksngl(i,spos=sposob,db=db)
			b = c.isit
			bulijan[i] = b
			if pt and b and not db: print c.printsingle(wsl,yrformlen=len(str(ey)))
			if pf and (not db) and not b: print c.printsingle(wsl,yrformlen=len(str(ey)))
			if db: print c.printsingle(wsl,yrformlen=len(str(ey))), "  ", c.polowyjoined

		self.bulijan = bulijan

	@property
	def outbulijan(self):
		return self.bulijan