#!/usr/local/bin/python3

from sys import argv, stdin

def parse(s, param):
    ptr = 0
    arr = [0] * param
    for i in range(0, len(s)-1, 6):
        cmd = s[i:i+6]
        if cmd == 'Masala':
            ptr += 1
        elif cmd == 'mAsala':
            ptr -= 1
        elif cmd == 'maSala':
            arr[ptr] += 1
        elif cmd == 'masAla':
            arr[ptr] -= 1
        elif cmd == 'masaLa':
            arr[ptr] = stdin.read(1)
        elif cmd == 'masalA':
            print (arr[ptr], end='', flush=True)
        else:
            print ('Invalid command at position: ' , i+1)
    print ('')

def help():
    print ('\nmasala-lang (0.0.1)\n')
    print ('usage: masala <filename>.masala <buffer length>')
    print ('example: masala hello.masala 100')

def main():
    if len(argv) == 3:
        filename = argv[1]
        param = int(argv[2])
        if filename[-7:] != '.masala':
            print("Invalid filename provided!")
            help()
            exit(1)
        else:
            with open(filename) as f:
                program = ""
                for line in f:
                    program += line
                program.strip('\n')
                if len(program) % 6 == 0 :
                    print("Syntax Error!")
                    exit(1)
                else:
                    parse(program, param)
    else:
        help()

if __name__ == '__main__':
    main()