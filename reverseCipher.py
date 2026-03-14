"""

Cracking Codes With Python

Chapter 4 - The Reverse Cipher

https://inventwithpython.com/cracking/chapter4.html

"""

reversedMessage = ""

message = input("Type your message to encrypt/decrypt: ")

i = len(message) - 1 # Negative Index for message
j = 0 # Index for message
k = 1 # Step counter

while i >= 0:
    reversedMessage = reversedMessage + message[i]
    print("Step", str(k), ":", message[j], "->", message[i], sep=" ")
    
    i -= 1
    j += 1
    k += 1

print()
print("Message length:", str(len(message)), sep=" ")
print("Result:", reversedMessage, sep=" ")
