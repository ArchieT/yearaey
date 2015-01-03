# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chksngl:
	def __init__(self,yr,spos,db):
		self.yr = yr
		self.spos = spos
		fs = "{0:b}"
		fos = fs.format(yr)
		self.fos = fos
		if spos=="bruteforcebyhalves" or db:
			#if yr==2991: print qwer # debug: crashing
			fo = list(fos)
			#print fos
			lfo = len(fo)
			plwni = float(lfo)/float(2)
			self.plwni = plwni
			if lfo % 2 == 0:
				polowa = []
				for i in xrange(0,int(plwni)):
					polowa.append(fo[i])
				polowb = []
				for i in xrange(int(plwni),lfo):
					polowb.append(fo[i])
			elif (lfo-1) % 2 == 0:
				polowa = []
				for i in xrange(0,int(plwni-0.5)):
					polowa.append(fo[i])
				polowb = []
				for i in xrange(lfo-1,int(plwni-0.5),-1):
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
		if (self.spos=="bruteforcebyreversing"): return (True if self.fos == self.fos[::-1] else False)
		elif (self.spos=="bruteforcebyhalves"): return (True if self.polowa == self.polowb else False)
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