# Program to convert plain text to ciphertext by A00279670

# Part 1
from string import ascii_lowercase

plaintext = input("Enter in plaintext text \n")
ciphertext = ""

for character in plaintext :
    ciphertext += ascii_lowercase[25-ascii_lowercase.index(character)]

print(ciphertext)


# Part 2
print("\nContinue to enter plain text. Enter -1 to end")
plaintext = ""
ciphertext_individual = ""
ciphertext_full = ""


while True:
    plaintext = input("")

    if plaintext == "-1":
        break
    if len(plaintext) > 1 :
        print("Enter one letter at a time")
        continue

    ciphertext_individual = ascii_lowercase[25-ascii_lowercase.index(plaintext)]
    ciphertext_full += ascii_lowercase[25-ascii_lowercase.index(plaintext)]
    print(ciphertext_individual)

print(ciphertext_full)
