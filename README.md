# Circuito Lógico Combinatorio - Restador de 03
## _Proyecto II - Fundamentos de Sistemas Computacionales (CE-1104)_
### Eduardo José Canessa Quesada & Luis Felipe Chaves Mena

Este proyecto consiste en diseñar y construir un circuito lógico combinatorio que reciba un número de 4-bits desde un computador. El número consta de un bit de habilitación y tres bits que representan un marcador previo a una penalización. El circuito debe decrementar en tres unidades el número recibido y mostrar el resultado en tres LEDs.

## Requisitos del Proyecto

- **Versión de Python**: Python 3.12.2 64-bit
- **IDE**: VSCode.
- **Microprocesador**: Raspberry Pi Pico W
- **Compilador del Microprocesador**: MicroPython, en los archivos se encuentra un documento de extensión _.micropico_, el cual es utilizado por VSCode para identificar el folder del proyecto. 
- **Elementos del Circuito**: El circuito lógico combinatorio utiliza compuertas lógicas AND, NOT y XOR. Además, requiere resistencias de 1/4 de potencia y LEDs.