#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ArchieT'

'''
*** Zadanie ***
Rok 2015 zapisany binarnie 11111011111 jest tak zwanym
palindromem (http://pl.wikipedia.org/wiki/Palindrom), tzn. wyrażeniem brzmiącym tak samo
niezależnie czy czytamy je od lewej do prawej czy od prawej do lewej.

Napisz program (w dowolnym języku programowania) który znajdzie wszystkie takie lata
(tzn. ich zapis binarny jest palindromem) od 2015 do 3015.
'''

# config:
defsy = 2015
defey = 3015

from sys import argv
import argparse
argh = argparse.ArgumentParser()
argg = argh.add_argument_group('OUTPUT types (you can choose more than one)')
argg.add_argument('-t','--printingtrue',action='store_true',help="Prints binary palyndomes as they are being found")
argg.add_argument('-f','--printingfalse',action='store_true',help="Prints what is found to not to be a binary palyndrome as it is being checked")
argg.add_argument('-l','--list',action='store_true',help="At the end, outputs a Python list containing decimal ints which are binary palindromes")
argg.add_argument('-d','--dict',action='store_true',help="At the end, outputs a Python dict with keys for each checked number and boolean values")
argga = argg.add_argument_group('singleprint parameters (for printingtrue and printingfalse)')
argga.add_argument('-w','--binarystringwithspacelength',type=int,help="Lenght of the binary string wth spaces (column width)",default=14)
argj = argh.add_argument_group('INPUT')
argj.add_argument('-s','--startyear',type=int,help="Start number (inclusively)",default=defsy)
argj.add_argument('-e','--endyear',type=int,help="End number (inclusively)",default=defey)
parmetry = vars(argh.parse_args())

if not(parmetry['printingtrue'] or parmetry['printingfalse'] or parmetry['list'] or parmetry['dict']):
	print "The results won't be displayed."
	print 'Look for output types in "%s --help"' % argv[0]

sy = parmetry['startyear']
ey = parmetry['endyear']

from ownlib.chkrng import chkrng
a = chkrng(sy, ey)
a.checkem(pt=(True if parmetry['printingtrue'] else False),pf=(True if parmetry['printingfalse'] else False),wsl=parmetry['binarystringwithspacelength'])

if parmetry['list'] or parmetry['dict']: bulijan = a.outbulijan

if parmetry['list']:
	tecosa = []
	for bulintidx in range(sy, ey + 1):
		if bulijan[bulintidx]: tecosa.append(bulintidx)
	print tecosa

if parmetry['dict']: print bulijan