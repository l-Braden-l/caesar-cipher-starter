#Braden Leach
#Oct 2 2024
#Caesar Cipher

#encrypt
    #variables
alphabet = 'abcdefghijklmonpqrstuvwxyz'
new_message =''

user_message = input('Enter your secret message: ').lower()
key = int(input('Enter a key: '))
for character in user_message:
    if character in alphabet:
        postion = alphabet.find(character)
        new_postion = (postion + key) % 26
        new_character = alphabet[new_postion]
        new_message += new_character
    else:
        new_message+= character
print('Your new message is ' + new_message)

#decrypt
    #variables
alphabet = 'abcdefghijklmonpqrstuvwxyz'
new_message =''

user_message = input('Enter your secret message: ').lower()
key = int(input('Enter a key: '))
for character in user_message:
    if character in alphabet:
        postion = alphabet.find(character)
        new_postion = (postion - key) % 26
        new_character = alphabet[new_postion]
        new_message += new_character
    else:
        new_message+= character
print('Your new message is ' + new_message)

