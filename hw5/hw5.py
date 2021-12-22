# Byeongchan Gwak, Student ID : 501026
# This serial library contains about serial connections.
# It allows reading and writing through the serial ports.
import serial 
import time

# Making a serial connection to write out through serial connection.
ser = serial.Serial(
        port='/dev/ttyS0',              # Define the serial port to read and write
        baudrate = 115200,              # I made a baudrate setting to 115200
        parity=serial.PARITY_NONE,      # For parity checking, but I set it 'No' 
        stopbits=serial.STOPBITS_ONE,   # Indicates the end of a character or the data transmission
        bytesize=serial.EIGHTBITS,      # The number of data bits
        timeout=1                       # The amount of time for before timing out
)

cmd='CSE467 Embedded Computing Systems. bcgwak\n'

while 1:
        # Write the cmd string value trough serial
        ser.write(cmd.encode())
        time.sleep(1)
