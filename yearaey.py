#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
__author__ = 'ArchieT'

# Program jest rozwiązaniem poniższego szkolnego zadania domowego.
# Napisano (większość) (rozpoczęto) w nocy z 2 na 3 stycznia 2015 roku i tegoż ranka wysłany do nauczyciela.

# This program is a school homework.
# It was written (mostly) (started) at night Jan 2-3, 2015, and sent to the teacher same morning.

'''
*** Zadanie ***
Rok 2015 zapisany binarnie 11111011111 jest tak zwanym
palindromem (http://pl.wikipedia.org/wiki/Palindrom), tzn. wyrażeniem brzmiącym tak samo
niezależnie czy czytamy je od lewej do prawej czy od prawej do lewej.

Napisz program (w dowolnym języku programowania) który znajdzie wszystkie takie lata
(tzn. ich zapis binarny jest palindromem) od 2015 do 3015.
'''

# config:
defsy = 2015  # default starting number
defey = 3015  # default ending number
defspos = "bruteforcebyreversing"  # default algorithm

from sys import argv
import argparse
argh = argparse.ArgumentParser(description="Program for finding palindromes in a specified range in a specified positional numeral system by the radix (from 2 to 36)")
argh.add_argument('-b','--baseposnumsys',type=int,choices=range(2,37),default=2,help="Choose base positional numeral system (by radix). [min: 2 max: 36] [default: 2 (binary)]")
argg = argh.add_argument_group('OUTPUT TYPES (you can choose more than one)')
argg.add_argument('-t','--printingtrue',action='store_true',help="Prints binary palindromes as they are being found")
argg.add_argument('-f','--printingfalse',action='store_true',help="Prints what is found to not to be a binary palindrome as it is being checked")
argg.add_argument('-l','--list',action='store_true',help="At the end, outputs a Python list containing decimal ints which are binary palindromes")
argg.add_argument('-d','--dict',action='store_true',help="At the end, outputs a Python dict with keys for each checked number and boolean values")
argg.add_argument('-g','--debug',action='store_true',help="Show how the analysis runs")
argga = argh.add_argument_group('=>singleprint parameters (for printingtrue and printingfalse)')
argga.add_argument('-w','--binstrwspacelen',type=int,help="Lenght of the binary number string with spaces (column width) [0=>auto] [default: 0]",default=0)
argj = argh.add_argument_group('INPUT')
argj.add_argument('-s','--startyear',type=int,help="Start number (inclusively) (default: %s)" % str(defsy),default=defsy)
argj.add_argument('-e','--endyear',type=int,help="End number (inclusively) (default: %s)" % str(defey),default=defey)
argk = argh.add_argument_group('PROCESSING')
argkk = argk.add_mutually_exclusive_group()
argkk.add_argument('-r','--bruteforcebyreversing',action='store_true',help="[default] Use the brute-force reversing algorithm")
argkk.add_argument('-p','--bruteforcebyhalves',action='store_true',help="Use the brute-force halving algorithm")
#arga = argh.add_argument_group('PROCESSING OPTIONS')
#argb = arga.add_mutually_exclusive_group()
#argb.add_argument('-z','--withzeros',action='store_true',help="Check for possibility of being a palindrome starting with zeros, for example 20(dec)=10100(bin)=0010100(bin) [default: no]")
argkj = argh.add_argument_group('DEBUG OPTIONS')
argkj.add_argument('-m','--timing',action='store_true',help="Show timing")
parmetry = vars(argh.parse_args())

if not(parmetry['printingtrue'] or parmetry['printingfalse'] or parmetry['list'] or parmetry['dict'] or parmetry['debug']):
	print "The results won't be displayed."
	print 'Look for output types in "%s --help"' % argv[0]

if parmetry['timing']:
	import time
	start_time = time.time()

spos = "bruteforcebyreversing" if parmetry['bruteforcebyreversing'] else ("bruteforcebyhalves" if parmetry['bruteforcebyhalves'] else defspos)

sy = parmetry['startyear']
ey = parmetry['endyear']

from ownlib.chkrng import chkrng
a = chkrng(sy, ey)
a.checkem(
	base=parmetry['baseposnumsys'],
	pt=(True if parmetry['printingtrue'] else False),
	pf=(True if parmetry['printingfalse'] else False),
	db=(True if parmetry['debug'] else False),
	sposob=spos,
	wsl=parmetry['binstrwspacelen']
)

if parmetry['list'] or parmetry['dict']: bulijan = a.outbulijan

if parmetry['list']:
	tecosa = []
	for bulintidx in ((range(sy, ey + 1)) if not (ey>999999 or ey-sy>800000) else (xrange(sy, ey + 1))):
		if bulijan[bulintidx]: tecosa.append(bulintidx)
	print tecosa

if parmetry['dict']: print bulijan

if parmetry['timing']: print("-- %s seconds --" % float(float(time.time())-float(start_time)))