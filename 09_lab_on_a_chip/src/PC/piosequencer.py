"""CircuitPython Essentials HID Keyboard example"""
import os
import time
import serial 
import serial.tools.list_ports
from functions import selectCOM, mkdir

QTPY_BOOT_PIN = 21

class sequencer():
    def __init__(self,dev):
        print("Init")
        try:
            self.ser = serial.Serial(dev, 115200, timeout = 0.001)
            # self.ser = serial.Serial(dev, 115200)
        except Exception as e:
            print("COM can not open,Exception = ", e)
        self.file = None

    def readIO(self, pin):
        res = self.__readIO(pin)
        while res == "":
            res = self.__readIO(pin)
        if res == '-':
            print('1')
        else:
            print('0')

    def __setPin(self, pin):
        s = 'p'+str(pin)
        self.ser.write(s.encode('utf-8'))
    def setPin(self, pin):
        self.__setPin(pin)

    def __writeIO(self, output=0):
        s = '>'+str(output)
        self.ser.write(s.encode('utf-8'))
        # self.ser.write('>'.encode('utf-8'))
        # self.ser.write(str(output).encode('utf-8'))
    
    def writeIO(self, output):
        self.__writeIO(output)
        print(self.ser.read())

    def __readIO(self, pin):
        def sendPin(__pin): # set pin
            self.ser.write('p'.encode('utf-8')) # io read identifier
            self.ser.write(str(__pin).encode('utf-8'))
            self.ser.write(b'\n') # scanf identifier
        sendPin(pin)
        self.ser.write(b'<') # io read identifier
        tmp = self.ser.read(2)
        if tmp == b'':
            return ""
        
        if tmp[1] == 49:
            return '-'
        else:
            return '_'

    # record at a least a few seconds of button input to your RP2040 (in RAM)   
    def record(self, seconds, frequency = 20):
        period = 1/frequency
        self.__setPin(QTPY_BOOT_PIN)
        filename = time.strftime("%m%d%H%M%S", time.localtime())  
        print(filename)
        with open('./records/'+filename+'.txt', 'w') as self.file:
            self.file.write(str(frequency)+'\n')
            start_t = time.time()
            while time.time() - start_t < seconds:
                smalltime = time.time()
                self.file.write(self.__readIO(QTPY_BOOT_PIN))
                while time.time() - smalltime < period:
                    continue
        print("Recorded\n")

    def loopRecord(): 
        print("Looping\n")   # loop the recording when play
    
    def saveRecord(path):
        print("Saved\n")

    # replay a recorded sequence on your NeoPixel
    def playRecord(self, filename, fre = 0, pin = QTPY_BOOT_PIN):
        starttime = time.time()
        with open('./records/'+filename+'.txt', 'r') as f:
            if fre == 0:
                period = 1/int(f.readline())
            else:
                period = 1/int(fre)

            print("period = ", period)
            all = f.read()
            print("size = ", len(all))
            if all[0] == '-':
                self.__writeIO(1)
            else:
                self.__writeIO(0) 
            for i in range(1, len(all)):
                smalltime = time.time()
                if all[i] != all[i-1]:
                    if all[i] == '-':
                        self.__writeIO(1)
                    elif all[i] == '_':
                        self.__writeIO(0)                 
                while time.time() - smalltime < period:
                    continue

        print("Replay time = ", time.time() - starttime)
        print("\n")

    def playloop(self, filename, pin = QTPY_BOOT_PIN):
        while True:
            self.playRecord(filename, pin)

    def readREG(self, address):
        s = 'r' + address + '\n'
        self.ser.write(s.encode('utf-8'))
        data = self.ser.readline()
        print("Read: ")
        print(data)
        print("\n")
        
    def writeREG(self, address, value):
        s = address +'\n' + value +'\n'
        self.ser.write('w'.encode('utf-8'))
        self.ser.write(s.encode('utf-8'))
        print("\n")

    def writei2c(self, address,value):
        s='o'+address+'\n'+value+'\n'
        self.ser.write(s.encode('utf-8'))
        
    def readi2c(self,address, readlen):
        s='i'+address+'\n'+readlen+'\n'
        self.ser.write(s.encode('utf-8'))
        tmp=self.ser.readline()
        res=tmp.split(',')
        for i in res:
            print(i)

if __name__ =="__main__":
    mkdir() #create folders for recordings 
    COM_list = selectCOM()
    seq = sequencer(COM_list[0])

    with open('./command.log', 'w') as f:
        f.write("=====start=====\n")

    while True:
        command = input()
        with open('./command.log', 'w') as f:
            s = time.strftime("%m,%d, %H:%M:%S", time.localtime()) + '\t' + command + '\n'
            f.write("s")
        args = command.split(" ")

        if args[0] == '#':              #  # seconds
            if len(args) == 2:
                seq.record(int(args[1]))
            elif len(args) == 3:
                seq.record(int(args[1]), int(args[2]))
        elif args[0]=='$':              #  $ filename
            if len(args) == 2:
                seq.playRecord(args[1])
            elif len(args) == 3:
                seq.playRecord(args[1], args[2])
        elif args[0] == 'r':            #  r address(%08x)
            seq.readREG(args[1])
        elif args[0] == 'w':            #  w address(%08x) value(%08x)
            seq.writeREG(args[1], args[2])
        elif args[0] == 'p':
            seq.setPin(args[1])
        elif args[0] == '>':
            seq.writeIO(args[1])
        elif args[0] == '<':
            seq.readIO(args[1])
        elif args[0] == 'e':
            exit()