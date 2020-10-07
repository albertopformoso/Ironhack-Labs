# Project: Message Encryption & Decryption

## Overview

The goal of this project is to generate a random sequence of codification to encrypt and decrypt a message in the running sesion.

---

## Game Design

The game has an input of multiple characters from a to z, A to Z, 0 to 9 and some symbols that are merged on a list and shuffled randomly. A random number is generated as a seed of the codification. Once the running sesion is ended the codification is lost and you could not decrypt a message you had anymore, this was implemented to protect the data in the sesion.

To use all the knowledge learnd during the week 1 in the program are implemented functions, classes, Regular Expresions, Bult-ins and Error Handling. 

The encriptation consist in take the random codification string and find a letter of your message on this string and displace to the right you letter n positions to get a new letter (this is generated 'n' number is generated at the begining of the program) the same method is used to decrypt, but the letter is displaced to the left.


## Software Archives

* `main.py` contains the main project.
* `Decrypt.py` contains a class that decrypts the message.


