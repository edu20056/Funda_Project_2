
import machine
import sys 
import time

# Hardware____________________________________________________________________________________________

# LED's
led = machine.Pin("LED", machine.Pin.OUT)

provee = machine.Pin(7, machine.Pin.OUT)

pin_lst = [15, 16, 17]
x_bit = [machine.Pin(pin, machine.Pin.OUT) for pin in pin_lst]

# Main Loop____________________________________________________________________________________________

loop = True

while loop:
    user_input = sys.stdin.readline().strip()
    
    if user_input == "None":
        provee.value(0)

    else:
        provee.value(1)

        try:
            number = int(user_input)
            binary = bin(number)[2:]
            digs = list(map(int, binary))[::-1]

            for index, led in enumerate(x_bit):
                try:
                    led.value(digs[index])
                    print(f"x_bit[{index}] : {digs[index]} -> LED : {led}")
                except IndexError:
                    led.value(0)
                    print(f"x_bit[{index}] : {0} -> LED : {led}")
        except ValueError:
            pass
    
    time.sleep(0.1)  



