# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class chksngl:
	def __init__(self,yr):
		fs = "{0:b}"
		self.yr = yr
		fos = fs.format(yr)
		fo = list(fos)
		print fos
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
				polowa.append(fo[i])
		elif (plwni-0.5).is_integer():
			#polowa = fo[int(lfo-(plwni)):]
			polowa = []
			for i in range(0,int(plwni-0.5)):
				polowa.append(fo[i])
			#polowb = fo[:int(lfo-(plwni))]
			polowb = []
			for i in range(lfo-1,int(plwni+1.5),-1):
				polowa.append(fo[i])
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
	def polowy(self):
		return {'a':self.polowa,'b':self.polowb}
	def isit(self):
		if self.polowa == self.polowb:
			return True
		else:
			return False