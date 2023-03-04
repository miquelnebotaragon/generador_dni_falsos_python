<h1 align="center"><b>Convertir vídeos de YouTube a mp3 amb Python</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://user-images.githubusercontent.com/57944755/209711233-15963b37-2a47-4d86-827d-fe5af86343b5.png"></div>

# 👁️‍🗨️ Introducció
Si es dona el cas que volem descarregar únicament l'àudio d'algun dels nostres vídeos favorits de YouTube, ho podem fer amb un recull senzill de línies de codi tal com veurem a l'exemple següent.

# 💻 Escenari
Kubuntu 22.04 LTS

# 0️⃣ Abans de començar
1. Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'ell i la seva versió mitjançant la comanda següent a dins el Terminal (Ctrl+Alt+T): 

```console
user@kubuntu-mnebot:~$ sudo python3 -V
```
Si no el tenim instal·lat, el podem aconseguir fàcilment mitjançant la comanda:
```console
user@kubuntu-mnebot:~$ sudo apt install python3
```
2. Per a la importació del mòdul necessari (**youtube_dl**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent manera:
```console
user@kubuntu-mnebot:~$ sudo apt install python3-pip
```
3. Instal·larem finalment el mòdul necessari responsable de la descàrrega i conversió del nostre vídeo:
```console
user@kubunu-mnebot:~$ sudo pip install youtube_dl
```

# 👇 Descàrrega i execució
Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **convertir_youtube_mp3.py**). Cal informar que la descàrrega dels àudios, per defecte, es farà al mateix directori on es trobi l’arxiu de Python, per això, hem d’assegurar-nos que disposi d’espai suficient pel seu emmagatzematge.
<p></p>📝 Descàrrega de l'arxiu .py des d'<a href="https://github.com/miquelnebotaragon/youtube_mp3_python/blob/main/convertir_youtube_mp3.py" target="_blank">aquí</a>.

# ➕ Informació
1️⃣ L'arxiu **.py** ha estat comentat al detall (#) per tal de possibilitar l'anàlisi del seu funcionament.<p></p>
2️⃣ Totes les descàrregues de vídeos de YouTube sense llicenciament Creative Commons són il·legals. Assegura't bé, abans de fer servir aquesta aplicació, que no infringeixes aquesta ni cap altra norma vigent.<p></p>
3️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni prejudicis que pugui provocar el seu ús.