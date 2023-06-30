## using the alphabet twice just incase we get a crazy value like 24
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(direction,text,shift):
    cipherText = ""
    decryptionText = ""
    if direction == "encode":
        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
        for value in text:
            index = alphabet.index(value)
            cipherText += alphabet[index + shift]
        print(f"Your encypted text is now: {cipherText}")
    if direction == "decode":
        for value in text:
            index = alphabet.index(value)
            decryptionText += alphabet[index - shift]
        print(f"Your decoded message is: {decryptionText}")

#decrypt or encrypt question
encode = True
while encode:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    encrypt(direction,text,shift)
    value = input("Would you like to encrypt or decrypt another word?\n (y/n):  ").lower()
    if value == "y":
        continue
    else:
        encode = False