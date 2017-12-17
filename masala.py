#!/usr/local/bin/python3

from sys import argv as MASALA
from sys import stdin as mAsala

def masalA(MAsala):
    maSala = 0
    masAla = [0] * 1024
    for masaLa in range(0, len(MAsala)-1, 6):
        if MAsala[masaLa:masaLa+6] == 'masala':
            print ('masala')
        elif MAsala[masaLa:masaLa+6] == 'Masala':
            maSala += 1
        elif MAsala[masaLa:masaLa+6] == 'mAsala':
            maSala -= 1
        elif MAsala[masaLa:masaLa+6] == 'maSala':
            masAla[maSala] += 1
        elif MAsala[masaLa:masaLa+6] == 'masAla':
            masAla[maSala] -= 1
        elif MAsala[masaLa:masaLa+6] == 'masaLa':
            masAla[maSala] = ord(mAsala.read(1))
        elif MAsala[masaLa:masaLa+6] == 'masalA':
            print (masAla[maSala], end='', flush=True)
        elif MAsala[masaLa:masaLa+6] == 'maSAla':
            print (chr(masAla[maSala]), end='', flush=True)
        else:
            print ('invalid masala at position: ' , i+1)
    print ('')

def masala():
    print ('\nmasala-lang (0.0.1)\n')
    print ('usage: masala <filename>.masala')
    print ('example: masala hello.masala')

if __name__ == '__main__':
    if len(MASALA) == 2:
        if MASALA[1][-7:] != '.masala':
            print ("invalid masala provided!")
            masala()
            exit(1)
        else:
            masAla = ''
            with open(MASALA[1]) as maSala:
                for masaLa in maSala:
                    masAla += masaLa
            masAla = masAla.replace(' ', '').replace('\n', '')
            if len(masAla) % 6 != 0 :
                print ("masala error!")
                exit(1)
            else:
                masalA(masAla)
    else:
        masala()
