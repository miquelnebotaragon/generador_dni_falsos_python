<h1 align="center"><b>Generador de números de DNI d'exemple amb Python</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://user-images.githubusercontent.com/57944755/223051160-9e5a1cdb-5bb7-4de8-b9a1-960865cade5f.png"></div>


# 👁️‍🗨️ Introducció
Generador de números de DNI d'exemple amb Python (⚠️ la lletra generada és aleatòria, no té per què coincidir amb l'algoritme lògic que existeix als documents oficials).

# 💻 Escenari
Kubuntu 22.04 LTS

# 0️⃣ Abans de començar
1. Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'ell i la seva versió mitjançant la instrucció següent a dins el Terminal (Ctrl+Alt+T): 

```console
user@kubuntu-mnebot:~$ sudo python3 -V
```
Si no el tenim instal·lat, el podem aconseguir fàcilment teclejant:
```console
user@kubuntu-mnebot:~$ sudo apt install python3
```
2. Per a la importació del mòdul necessari (**random**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent manera:
```console
user@kubuntu-mnebot:~$ sudo apt install python3-pip
```
3. Instal·larem finalment el mòdul necessari responsable de la descàrrega i conversió del nostre vídeo:
```console
user@kubunu-mnebot:~$ sudo pip install random
```

# 👇 Descàrrega i execució
Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **generador_numeros_dni.py**).
<p></p>📝 Descàrrega de l'arxiu .py des d'<a href="https://github.com/miquelnebotaragon/generador_dni_falsos_python/blob/main/generador_numeros_dni.py" target="_blank">aquí</a>.

# 🏆 Vull saber-ne més
Desglossant el codi:
## Part 1:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import random

```
Aquesta és la part inicial i més senzilla:
<p>· Enumeram els mòduls a importar, en aquest cas només un, random.</p>


```python

# Variables:
num_elements = int(input("Introdueix el nombre de números de DNI aleatoris a generar: "))
llistat = [str(random.randint(10000000, 99999999)) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(num_elements)]

```

<p>· Mostram en pantalla un text on sol·licitam a l'usuari que indiqui la quantitat de números falsos que vol generar.</p>
<p>· La segona variable s'emmagatzemarà de manera automàtica generant-se un llistat amb la quantitat indicada de números falsos + lletra tot tenint present la quantitat indicada anteriorment.</p>

## Part 2:
```python

# Execució:
for elements in llistat:
    print(elements)

```

<p>· Finalment procedim a l'execució del programa imprimint en pantalla el llistat emmagatzemat a la segona variable.</p>

# ➕ Informació
1️⃣ L'arxiu **.py** ha estat comentat al detall (#) per tal de possibilitar l'anàlisi del seu funcionament.<p></p>
2️⃣ Totes les descàrregues de vídeos de YouTube sense llicenciament Creative Commons són il·legals. Assegura't bé, abans de fer servir aquesta aplicació, que no infringeixes aquesta ni cap altra norma vigent.<p></p>
3️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni prejudicis que pugui provocar el seu ús.
