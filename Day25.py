#!/usr/bin/env python

from AOC2019 import IntcodeV3, readIntcodeProg
import cmd

prog = readIntcodeProg("input25.txt")
d = IntcodeV3(prog,"DROID",[])

def sendToProgram(command):
    print(command)
    asc = command2ASCII(command)
    d.setInputs(asc)
    d.runProgram()
    printASCII(d.getOutput())

def command2ASCII(command):
    asc = []
    for c in command:
        asc.append(ord(c))
    asc.append(10)
    return asc

def printASCII(o):
    for i in o:
        if (i!=10):
            print(chr(i),end="")
        else:
            print("")

class Droid(cmd.Cmd):
    prompt = '(DROID) '
    
    def do_go(self,arg):
        command = arg # north, south, east, or west
        sendToProgram(command)

    def do_north(self,arg):
        sendToProgram('north')

    def do_south(self,arg):
        sendToProgram('south')

    def do_east(self,arg):
        sendToProgram('east')

    def do_west(self,arg):
        sendToProgram('west')

    def do_n(self,arg):
        sendToProgram('north')

    def do_s(self,arg):
        sendToProgram('south')

    def do_e(self,arg):
        sendToProgram('east')

    def do_w(self,arg):
        sendToProgram('west')
        
    def do_take(self,arg):
        command = "take "+arg
        sendToProgram(command)
    
    def do_drop(self,arg):
        command = "drop "+arg
        sendToProgram(command)
    
    def do_inv(self,arg):
        command = "inv"
        sendToProgram(command)

    def do_list(self,arg):
        command = "inv"
        sendToProgram(command)  


if __name__ == '__main__':
    Droid().cmdloop()




