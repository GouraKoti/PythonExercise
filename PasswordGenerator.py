import random as rd
import string

length = 0

while length < 6:
    length = int(input("How long to be the password?\n"))
    if length<6:
        print ("Password length should be minimum 6 characters\n")
        continue
    
n_char,n_num = map(int,input("How many letters and digits the password should have? (hint:enter two digits with space)\n").split())


letters = rd.choices(string.ascii_letters,k=n_char)

numbers=rd.choices(string.digits,k=n_num)

n_sym = length-(n_char+n_num)
symbols=rd.choices(string.punctuation,k=n_sym)


password=(letters+numbers+symbols)
rd.shuffle(password)
password=''.join(password)

print(" \n Random password generator for you "+ password)
