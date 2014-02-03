# -*- coding: utf-8 -*-

#  IS-105 LAB2

import sys

gruppe = {  'student1': 'Simon Wik Eriksen', \
		'student2': 'Minh Nguyen Dinh', \
}

# Oppgave 1: Printer ut ascii fugl


def ascii_fugl():
	print 	"""
	 \/_
      \, /( ,/
       \\\\' ///
	\_ /_/
	(./
	 '`
		"""
pass

# Oppgave 2 & 3: returnerer verdiene x og y, definert nedenfor

def bitAnd(x, y):
	return x&y

# Oppgave 4: returnerer verdiene x og y, definert nedenfor

def bitXor(x, y):
	return x^y

# Oppgave 5: returnerer verdiene x og y, definert nedenfor

def bitOr(x, y):
	return x| y

# Oppgave 6: Returnerer bokstaven som bineær kode.

def ascii8Bin(bokstav):

	binary = ord(bokstav)

	return '{0:08b}'.format(binary)

# Oppgave 7: Printer ut en setning som bineær kode.

def transferBin(string): 
	l = list(string)
	for c in l:
		#if c != "None":
		print ascii8Bin(c)
	pass
		
# Oppgave 8: Printer ut en bokstav som hexadesimalt kode

def ascii2Hex(bokstav):

	hexy = ord(bokstav)

	return '{0:02x}'.format(hexy)

def transferHex(string): #printer ut en setning som hexadesimal kode
	l = list(string)
	for c in l:
		#if c != "None":
		print ascii8Bin(c)
	pass




 #verdiene defineres til oppgavene 2&3 til 5
Xor = bitXor(4, 5)
Or = bitOr (0, 1)
And = bitAnd (6, 5)

#run oppg. 1
print "\n\n# Oppgave 1"
print "\nascii_fugl() resultat:"
ascii_fugl()


#run oppg. 2 & 3
print "\n\n# Oppgave 2 & 3"
print "\nbitAnd(6, 5) = %d" % (And)


#run oppg. 4
print "\n\n# Oppgave 4"
print "\nbitXor(4, 5) = %d" % (Xor)

#run oppg. 5
print "\n\n# Oppgave 5"
print "\nbitOr(0, 1) = %d" % (Or)

#run oppg. 6
print "\n\n# Oppgave 6"
print "\nascii8Bin('A') resultat:"
print ascii8Bin("A")

#run oppg. 7
print "\n\n# Oppgave 7"
print "\ntransferBin(\"test\") resultat:"
transferBin("test")

#run oppg. 8
print "\n\n# Oppgave 8"
print "\nascii2Hex('A') resultat:"
print ascii2Hex('A')

print "\ntransferHex('tester igjen') resultat:"
transferHex('tester igjen')

