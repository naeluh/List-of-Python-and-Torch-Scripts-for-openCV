import serial
from g1_arduino_working import space
ser = serial.Serial("/dev/ttyUSB0", 9600) # Establish the connection on a specific port
#counter = 32 # Below 32 everything in ASCII is gibberish

while True:
    arduino = len(ser.readline())
    if arduino > 0:
		space()
    print ser.readline()
     #sleep(.1) # Delay for one tenth of a second
     #if counter == 255:
      #counter = 32