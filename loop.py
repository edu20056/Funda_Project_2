
import serial

s = serial.Serial("COM11", 115200)

def raspberry(number):
    s.write(f"{number}\n".encode())

while True:
    try:
        
        print("------------------------------------")
        user_input = int(input("Input .: "))
        result = user_input - 3

        if 0 <= user_input < 8:
                
            print(f"Decimal -> {user_input} - 3 = {result}")

            if result < 0:
                result = 5 + user_input
                print(f"[Número Negativo] Complemento a Dos de {result - 5} con tres dígitos -> {bin(user_input)[2:]} + 101 = {bin(result)[2:]}")
                
            print(f"Binario -> {bin(user_input)[2:]} - 011 = {bin(result)[2:]}")
            
            raspberry(user_input)
        
        else:
            print("-1 !Error : El número debe estar en el rango [0, 8[")
        
    except ValueError:
        raspberry(None)
        