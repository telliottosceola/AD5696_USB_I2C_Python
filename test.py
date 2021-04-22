import serial
import time

port = 'COM3'

command_one = [0xAA,0x05,0xBE,0x0C,0x31,0x00,0x00,0xAA] #set output 1 to 0
command_two = [0xAA,0x05,0xBE,0x0C,0x31,0xFF,0xFF,0xA8] #set output 1 to full

off = [0x00,0x00]
full = [0xFF, 0xFF]

serial_port = serial.Serial(port, baudrate=115200, bytesize=8, stopbits=1, timeout=.5)

# serial_port.open()

def writeI2C(address, register, data):
    payloadLen = len(data)+3
    writeData = [0xAA, payloadLen, 0xBE, address, register]
    for x in data:
        writeData.append(x)
    checksum = 0
    for x in writeData:
        checksum += x
    checksum = checksum&255
    writeData.append(checksum)
    return writeData

while(True):
    serial_port.write(writeI2C(0x0C,0x31,full))
    time.sleep(2)
    serial_port.write(writeI2C(0x0C,0x31,off))
    time.sleep(2)
