#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ArchieT'

'''*** Zadanie ***
Rok 2015 zapisany binarnie 11111011111 jest tak zwanym
palindromem (http://pl.wikipedia.org/wiki/Palindrom), tzn. wyrażeniem brzmiącym tak samo
niezależnie czy czytamy je od lewej do prawej czy od prawej do lewej.

Napisz program (w dowolnym języku programowania) który znajdzie wszystkie takie lata
(tzn. ich zapis binarny jest palindromem) od 2015 do 3015.'''

#config:
printingtrue = True
printingfalse = False
sy = 2015
ey = 3015

fs = "{0:b}"
tecosa = []
bulijan = {}

for i in range(sy,ey+1):
	print i
	fos = fs.format(i)
	fo = list(fos)
	print fos
	lfo = len(fo)
	plwni = float(lfo)/float(2)
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
	if polowa == polowb:
		bulijan[i] = True
		tecosa.append(i)
		print polowa, polowb, True, plwni
	else:
		bulijan[i] = False
		print polowa, polowb, False, plwni
print tecosa
print bulijan

