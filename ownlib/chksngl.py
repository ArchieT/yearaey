# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chksngl:
	def __init__(self,yr):
		fs = "{0:b}"
		self.yr = yr
		#if yr==2991: print qwer # debug: crashing
		fos = fs.format(yr)
		fo = list(fos)
		#print fos
		self.fos = fos
		lfo = len(fo)
		plwni = float(lfo)/float(2)
		self.plwni = plwni
		if plwni.is_integer():
			polowa = []
			for i in range(0,int(plwni)):
				polowa.append(fo[i])
			polowb = []
			for i in range(int(plwni),lfo):
				polowb.append(fo[i])
		elif (plwni-0.5).is_integer():
			polowa = []
			for i in range(0,int(plwni-0.5)):
				polowa.append(fo[i])
			polowb = []
			for i in range(lfo-1,int(plwni-0.5),-1):
				polowb.append(fo[i])
			#polowb = polowb[::-1]
		else:
			raise ValueError
		self.polowa = polowa
		self.polowb = polowb[::-1]
	@property
	def polowy(self): return {'a':self.polowa,'b':self.polowb}
	@property
	def polowyjoined(self): return {'a':''.join(self.polowa),'b':''.join(self.polowb)}
	@property
	def isit(self): return True if self.polowa == self.polowb else False
	def printsingle(self,wspaceslen):
		def spaporbp(ilemabyc,cojest):
			ilejest = len(cojest)
			brakuje = ilemabyc-ilejest
			halfbrakuje = (float(brakuje)/float(2))
			if halfbrakuje.is_integer():
				a = b = (' '*int(halfbrakuje))
			elif (halfbrakuje+0.5).is_integer():
				a = (' '*int(halfbrakuje-0.5))
				b = a+' '
			return a+cojest+b
		binarprint = self.fos if wspaceslen<len(self.fos) else spaporbp(wspaceslen,self.fos)
		print "%4d  | %s |  %s" % (self.yr,binarprint,self.isit)