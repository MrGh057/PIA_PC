import math

def encrypt(correocryp, clave):
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    myKey = len(clave)

    ciphertext = encryptMessage(myKey, correocryp)
    
    return ciphertext

def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
        
            ciphertext[column] += message[currentIndex]

            currentIndex += key

    return ''.join(ciphertext)

def descryp(correodes, clave):
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    myKey = len(clave)

    plaintext = decryptMessage(myKey, correodes)

    print("Correo: "+ plaintext)


def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    
    numOfRows = key
    
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    correocryp = input('Ingrese el correo: ')
    clave = input('Ingresa tu palabra clave para cifrar: ')
    correocry = encrypt(correocryp=correocryp, clave=clave)
    print ("Correo encriptado: " + correocry)

    while True:
        des = input("Desencriptar correo: S | N  ")
        if des == "S":
            descryp(correodes=correocry, clave=clave)
        elif des == "N":
            break
