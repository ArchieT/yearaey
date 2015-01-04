# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chksngl:
	def __init__(self,yr,spos,db,base,zer):
		self.yr = yr
		self.niejest = True if yr % base == 0 and not zer else False
		self.zer = zer
		self.spos = spos
		fos = self.makefos(yr,base)
		self.fos = fos
		if spos=="bruteforcebyhalves" or db:
			self.polowienie(foss=fos)
	@staticmethod
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
	def polowienie(self,foss):
		# if yr==2991: print qwer # debug: crashing
		fo = list(foss)
		#print fos
		lfo = len(fo)
		plwni = float(lfo) / float(2)
		self.plwni = plwni
		if lfo % 2 == 0:
			polowa = []
			for i in range(0, int(plwni)):
				polowa.append(fo[i])
			polowb = []
			for i in range(int(plwni), lfo):
				polowb.append(fo[i])
		elif (lfo - 1) % 2 == 0:
			polowa = []
			for i in range(0, int(plwni - 0.5)):
				polowa.append(fo[i])
			polowb = []
			for i in range(lfo - 1, int(plwni - 0.5), -1):
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
		if self.niejest: return False
		if self.spos=="bruteforcebyreversing":
			a = True if self.fos == self.fos[::-1] else False
			if self.zer: self.ilezer = 0
			if a or not self.zer: return a
			else: fos = self.fos
			c = 0
			while not a:
				c+=1
				if fos[-c]=='0': fos='0'+fos
				a = True if fos == fos[::-1] else False
				if a:
					self.ilezer = c
					return True
				elif c+1>float(len(self.fos))/float(2): return False
		elif self.spos=="bruteforcebyhalves":
			a = True if self.polowa == self.polowb else False
			if self.zer: self.ilezer = 0
			if a or not self.zer: return a
			else:
				pa = self.polowa
				pb = self.polowb
			c=0
			while not a:
				c+=1
				if pb[c]=='0': pb = pa.pop()+pb
				a = True if pa==pb else False
				if a:
					self.ilezer = c
					return True
				elif c+1>len(self.polowb): return False
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
		fose = ('0'*self.ilezer)+self.fos if self.zer else self.fos
		binarprint = fose if wspaceslen<len(fose) else spaporbp(wspaceslen,fose)
		return " %s  | %s |  %s " % (yrformat,binarprint,self.isit)