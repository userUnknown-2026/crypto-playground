"""

Chapter 5 - Caesar Cipher

https://inventwithpython.com/cracking/chapter5.html

"""

import traceback

# Only these symbols will be encrypted/decrypted
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
          "abcdefghijklmnopqrstuvwxyz" \
          "0123456789" \
          "!\"§$%&/()=?`´#'-_.:,;\\{}[]|<>"

minKey = 0
maxKey = len(SYMBOLS) - 1

modeDescription = {
                    1: "Encrypt",
                    2: "Decrypt"
}

# Retrieve and validate cipher key
def get_cipher_key(minValue, maxValue):
    isValid = False

    while not isValid:
        userInput = input(f"Enter a cipher key [{minValue}-{maxValue}]: ")

        try:
            key = int(userInput)

            if minValue <= key <= maxValue:
                return key
            else:
                print("Key out of bounds. Please enter a valid whole number.")
                
        except ValueError:
            print("Wront input. Please enter a whole number.")


# Retrieve and validate en-/decryption mode
def get_mode():
    isValid = False

    while not isValid:
        userInput = input("Enter whether you want to encrypt [1] or decrypt [2]: ")

        try:
            mode = int(userInput)
            
            if mode == 1 or mode == 2:
                return mode
            else:
                print("Mode out of bounds. Please enter a valid whole number.")

        except ValueError:
            print("Wront input. Please enter a whole number.")

# Encrypt or decrypt message
def translate_message(message, key, mode):
    try:
        translated = ""
        
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)

                # Perform encryption
                if mode == 1:
                    translatedIndex = symbolIndex + key
                # Perform decryption
                elif mode == 2:
                    translatedIndex = symbolIndex - key

                # Handling if translatedIndex gets out of bounds
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)
                    
                translated = translated + SYMBOLS[translatedIndex]
                
            # Add symbol to translated message if not in SYMBOLS
            else:
                translated = translated + symbol

        return translated
    
    except Exception:
        print("An error occurred!")
        traceback.print_exc()

# Get message
userMessage = input("Enter your message to(de-)cipher: ")

# Get key
userKey = get_cipher_key(minKey, maxKey)

# Get mode
userMode = get_mode()

# "Translate" message
translatedMessage = translate_message(userMessage, userKey, userMode)

print(f"Process done.\n\n" 
      f"Input message: {userMessage}\n" 
      f"Key: {userKey}\n" 
      f"Mode: {modeDescription[userMode]}\n" 
      f"Output message: {translatedMessage}")
