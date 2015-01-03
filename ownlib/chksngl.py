# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chksngl:
	def __init__(self,yr,spos,db):
		self.yr = yr
		self.spos = spos
		fs = "{0:b}"
		fos = fs.format(yr)
		self.fos = fos
		if spos=="bruteforce" or db:
			#if yr==2991: print qwer # debug: crashing
			fo = list(fos)
			#print fos
			lfo = len(fo)
			plwni = float(lfo)/float(2)
			self.plwni = plwni
			if lfo % 2 == 0:
				polowa = []
				for i in range(0,int(plwni)):
					polowa.append(fo[i])
				polowb = []
				for i in range(int(plwni),lfo):
					polowb.append(fo[i])
			elif (lfo-1) % 2 == 0:
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
	def isit(self):
		if (self.spos=="divisibility"): return (True if ((int(self.fos) % 11 == 0) and (self.yr % 3 == 0)) else False)
		elif (self.spos=="bruteforce"): return (True if self.polowa == self.polowb else False)
	def printsingle(self,wspaceslen,yrformlen=7):
		import re
		yrformat = (re.sub(r'Q',str(int(yrformlen)),r"{:Qd}")).format(self.yr)
		#print str(int(yrformlen))
		def spaporbp(ilemabyc,cojest):
			ilejest = len(cojest)
			brakuje = ilemabyc-ilejest
			halfbrakuje = (float(brakuje)/float(2))
			if brakuje % 2 == 0:
				a = b = (' '*int(halfbrakuje))
			elif (brakuje+1) % 2 == 0:
				a = (' '*int(halfbrakuje-0.5))
				b = a+' '
			return a+cojest+b
		binarprint = self.fos if wspaceslen<len(self.fos) else spaporbp(wspaceslen,self.fos)
		return " %s  | %s |  %s " % (yrformat,binarprint,self.isit)