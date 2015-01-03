# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chkrng:
	def __init__(self,sy,ey):
		if not (isinstance(sy,int) and isinstance(ey,int)):
			raise ValueError
		else:
			self.sy = sy
			self.ey = ey
	def checkem(self,base=2,pt=True,pf=False,db=False,sposob='bruteforcebyreversing',wsl=None):
		sy = self.sy
		ey = self.ey

		bulijan = {}

		from ownlib.chksngl import chksngl
		if wsl is None or wsl==0:
			if 0<=self.ey<base: wsl = 1+2
			else:
				num=self.ey
				lco = 0
				while num!=0:
					num,asd=divmod(num,base)
					lco+=1
				wsla = lco+2
		elif isinstance(wsl,int) and wsl>0: wsla=wsl
		for i in range(sy,ey+1):
			#print i
			c = chksngl(i,spos=sposob,db=db,base=base)
			b = c.isit
			bulijan[i] = b
			if pt and b and not db: print c.printsingle(wsla,yrformlen=len(str(ey)))
			if pf and (not db) and not b: print c.printsingle(wsla,yrformlen=len(str(ey)))
			if db: print c.printsingle(wsla,yrformlen=len(str(ey))), "  ", c.polowyjoined
		self.bulijan = bulijan

	@property
	def outbulijan(self):
		return self.bulijan