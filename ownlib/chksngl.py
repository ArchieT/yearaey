# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chksngl:
	def __init__(self,yr):
		fs = "{0:b}"
		self.yr = yr
		fos = fs.format(yr)
		fo = list(fos)
		#print fos
		self.fos = fos
		lfo = len(fo)
		plwni = float(lfo)/float(2)
		self.plwni = plwni
		if plwni.is_integer():
			#polowa = fo[int(lfo-plwni):]
			polowa = []
			for i in range(0,int(plwni)):
				polowa.append(fo[i])
			#polowb = fo[:int(lfo-plwni)]
			polowb = []
			for i in range(int(plwni),lfo):
				polowb.append(fo[i])
		elif (plwni-0.5).is_integer():
			#polowa = fo[int(lfo-(plwni)):]
			polowa = []
			for i in range(0,int(plwni-0.5)):
				polowa.append(fo[i])
			#polowb = fo[:int(lfo-(plwni))]
			polowb = []
			for i in range(lfo-1,int(plwni-0.5),-1):
				polowb.append(fo[i])
		else:
			raise ValueError
		#if polowa == polowb:
		#	bulijan[i] = True
		#	tecosa.append(i)
		#	print polowa, polowb, True, plwni
		#else:
		#	bulijan[i] = False
		#	print polowa, polowb, False, plwni
		self.polowa = polowa
		self.polowb = polowb
	@property
	def polowy(self): return {'a':self.polowa,'b':self.polowb}
	@property
	def polowyjoined(self): return {'a':str.join(self.polowa),'b':str.join(self.polowb)}
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
		print "%4d | %s | %s" % (self.yr,binarprint,self.isit)