import random
char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
char_lenght = int(input("Şifreniz kaç karakter olsun? "))
password = ""   
for i in range(char_lenght):
    password += random.choice(char)

print("Şifreniz:", password)
