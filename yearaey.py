#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ArchieT'

#Wiadomość o zadaniu przeczytano o godzinie 23:20 2014-01-22, pracę rozpoczęto 23:22
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
	fo = fs.format(i)
	print fo
	lfo = len(fo)
	plwni = float(lfo)/float(2)
	if plwni.is_integer():
		polowa = fo[int(lfo-plwni):]
		polowb = fo[:int(lfo-plwni)]
	elif (plwni-0.5).is_integer():
		polowa = fo[int(lfo-(plwni)):]
		polowb = fo[:int(lfo-(plwni))]
	else:
		raise ValueError
	if polowa == polowb:
		bulijan[i] = True
		tecosa.append(i)
		print polowa, polowb, True
	else:
		bulijan[i] = False
		print polowa, polowb, False
print tecosa
print bulijan

