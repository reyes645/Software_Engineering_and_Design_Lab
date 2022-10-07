import database
import math
import random

def customEncrypt(inputText, N, D):  #Task 1
    err1 = ' '
    err2 = '!'
    if err1 in inputText or err2 in inputText:
        raise TypeError("Error, contains space or !")

    if N < 1:
        raise TypeError("Error, N needs to be >= 1")

    reverseTxt = inputText[::-1]

    if D == 1:  # Rightshift
        list = []
        list[:0] = reverseTxt
        length = len(list)
        rightTxt = []
        for i in range(len(reverseTxt)):
            list.append(chr(ord(list[i]) + N))
            rightTxt.append(list[i + length])
            rightString = ''.join(rightTxt)
        return rightString

    elif D == -1:  # Leftshift
        list = []
        list[:0] = reverseTxt
        length = len(list)
        leftTxt = []
        for i in range(len(reverseTxt)):
            list.append(chr(ord(list[i]) - N))
            leftTxt.append(list[i + length])
            leftString = ''.join(leftTxt)
        return leftString

    else:
        raise TypeError("Error: Direction not 1 or -1 indicating right or left.")

def testCustomEncrypt(): #Task 2
    while True:
        try:
            print("Testing Custom Encryption Algorithm")
            x = input("Enter UserID as text :  ")
            y = input("Enter password as text :  ")
            n = int(input("Enter N please. "))
            d = int(input("Enter D please. "))
            encryptedUsertext = customEncrypt(x, n, d)
            encryptedpasstext = customEncrypt(y, n, d)
            break
        except Exception:
            print("Error: Invalid Arguments. Please Try Again")
            continue
        finally:
            pass

    print("encrypted userid: " + encryptedUsertext)
    print("encrypted password: " + encryptedpasstext)

    if d == 1:
        cipherUsertext = customEncrypt(encryptedUsertext, n , -1)
        cipherpasstext = customEncrypt(encryptedpasstext, n, -1)
    elif d == -1:
        cipherUsertext = customEncrypt(encryptedUsertext, n, 1)
        cipherpasstext = customEncrypt(encryptedpasstext, n, 1)

    print("Original userid: " + cipherUsertext)
    print("Original passwd: " + cipherpasstext)

    return



def uniq_num():
    digits = [i for i in range(0, 10)]
    randstr = ''
    for i in range(6):
        index = math.floor(random.random() * 10)
        randstr += str(digits[index])
    unique_id = int(randstr)
    return unique_id
def proj_encrypt(): #implements
    #Need implentation
    #unique_id will be numbers only 6 digits
    unique_id = uniq_num()

    #while unique_id is not unique from searching proj database, repeat uniq_num() function.

    return unique_id
