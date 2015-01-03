# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chksngl:
	def __init__(self,yr,spos,db,base):
		self.yr = yr
		self.spos = spos
		fos = self.makefos(yr,base)
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
	def makefos(yr,base):
		if base==2 or base==8 or base==16:
			fs = "{0:b}" if base==2 else "{0:o}" if base==8 else "{0:x}" if base==16 else None
			fos = fs.format(yr)
		elif base==10:
			fos = str(yr)
		elif type(base)==int and base<36 or base==36:
			alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
			ac = alphabet[:base]
			if not isinstance(yr,(int,long)):
				raise TypeError('Number must be an integer')
			out = ''
			if 0 <= yr < base:
				return ac[yr]
			num=yr
			while num!=0:
				num,ij=divmod(num,base)
				out=ac[ij]+out
			fos = out
		return fos
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