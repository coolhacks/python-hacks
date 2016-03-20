#!/usr/bin/env python
# -*- coding: cp1252 -*-

__VERSION__ = '1.0'
import immlib
from immlib import BpHook
DESC = "Simple PyHook" 


class DemoHook(BpHook): 
    def __init__(self):
        BpHook.__init__(self)


    def run(self, regs):
	imm = immlib.Debugger()
	eipOnStack = imm.readLong(regs['ESP'])
	strcpyFirstArg =  imm.readLong(regs['ESP'] + 4)
	strcpySecondArg = imm.readLong(regs['ESP'] + 8) #En este caso, nos interesa la funci�n strcpy
	imm.log("EIP on the stack 0x%80x First Arg: 0x%08x Second Arg: 0x%08x "%(eipOnStack, strcpyFirstArg, strcpySecondArg))
	receivedString = imm.readString(strcpySecondArg)
	imm.log("Received String %s with length %d " %(str(receivedString), len(receivedString))) #Aqu� pintamos en la pesta�a de logs, los argumentos que se han enviado a la funci�n.
	imm.updateLog() 
		
def main(args):
   imm = immlib.Debugger()
   functionToHook = "msvcrt.strcpy" #En sistemas windows, la funci�n STRCPY 
   functionAddress = imm.getAddress(functionToHook) #En esta linea recuperamos la direcci�n de memoria donde se encuentra cargada la funci�n STRCPY
   newHook = DemoHook()
   newHook.add("Demo Hook", functionAddress)
   return "Success!"
