#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import random

# Variables:
num_elements = int(input("Introdueix el nombre de números de DNI aleatoris a generar: "))
llistat = [str(random.randint(10000000, 99999999)) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(num_elements)]

# Execució:
for elements in llistat:
    print(elements)
