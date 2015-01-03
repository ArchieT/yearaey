yearaey
=======

Program for finding palindromes in a specified range in a specified positional numeral system by the radix (from 2 to 36).

It was a school homework, done at night Jan 2-3, 2015. 

Because of the malefficiency of the calculations-based alghorithms, the program gives supports only the following brute-force alghorithms:
 * brute-force by reversing — it just reverses the string and checks if it is still the same string
 * brute-force by halving — it divides the string into two strings, reverses the second one and checks whether they're equal. If the lenght of the string is odd, the number in the center is not considered.

The program doesn't consider whether a number is a palindrome beginning with zeros — so there, all of the palindromes will actually be indivisible by the radix.

 
###Help
```
usage: ./yearaey.py [-h]
                  [-b {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36}]
                  [-t] [-f] [-l] [-d] [-g] [-w BINSTRWSPACELEN] [-s STARTYEAR]
                  [-e ENDYEAR] [-r | -p] [-m]

Program for finding palindromes in a specified range in a specified positional
numeral system by the radix (from 2 to 36)

optional arguments:
  -h, --help            show this help message and exit
  -b {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36}, --baseposnumsys {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36}
                        Choose base positional numeral system (by radix).
                        [min: 2 max: 36] [default: 2 (binary)]

OUTPUT TYPES (you can choose more than one):
  -t, --printingtrue    Prints binary palindromes as they are being found
  -f, --printingfalse   Prints what is found to not to be a binary palindrome
                        as it is being checked
  -l, --list            At the end, outputs a Python list containing decimal
                        ints which are binary palindromes
  -d, --dict            At the end, outputs a Python dict with keys for each
                        checked number and boolean values
  -g, --debug           Show how the analysis runs

=>singleprint parameters (for printingtrue and printingfalse):
  -w BINSTRWSPACELEN, --binstrwspacelen BINSTRWSPACELEN
                        Lenght of the binary number string with spaces (column
                        width) [0=>auto] [default: 0]

INPUT:
  -s STARTYEAR, --startyear STARTYEAR
                        Start number (inclusively) (default: 2015)
  -e ENDYEAR, --endyear ENDYEAR
                        End number (inclusively) (default: 3015)

PROCESSING:
  -r, --bruteforcebyreversing
                        [default] Use the brute-force reversing algorithm
  -p, --bruteforcebyhalves
                        Use the brute-force halving algorithm

PROCESSING SETTINGS:
  [it will be possible to check for possibility of being a palindrome starting with zeros, for example 20(dec)=10100(bin)=0010100(bin), coming soon]

DEBUG OPTIONS:
  -m, --timing          Show timing
```
