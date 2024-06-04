
import serial

s = serial.Serial("COM11", 115200)

def raspberry(number):
    s.write(f"{number}\n".encode())

while True:
    try:
        
        user_input = int(input("Input .: "))

        if 0 <= user_input < 8:
            raspberry(user_input)
        else:
            print("-1 !Error : El número debe estar en el rango [0, 8[")
        
    except ValueError:
        print("-1 !Error : Input inválido")
