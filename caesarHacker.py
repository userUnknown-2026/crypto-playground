"""

Chapter 6 - Hacking the Caesar Cipter with Brute-Force

https://inventwithpython.com/cracking/chapter6.html

"""

SYMBOLS =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
            "abcdefghijklmnopqrstuvwxyz" \
            "1234567890" \
            "!\"§$%&/()=?`´+#*'~,.-;:_<>|^°@µ€²³{}[]\\"

def decrypt_cipherText():
    try:
        cipherText = input("Enter the ciphertext to decrypt: ")
        
        for key in range(len(SYMBOLS)):
            clearText = ""
            
            for symbol in cipherText:
                if symbol in SYMBOLS:
                    symbolIndex = SYMBOLS.find(symbol)
                    decryptedIndex = symbolIndex - key

                    if decryptedIndex < 0:
                        decryptedIndex = decryptedIndex + len(SYMBOLS)

                    clearText = clearText + SYMBOLS[decryptedIndex]
                    
                else:
                    clearText = clearText + symbol

            print("KEY: %s -> DECRYPTED: %s" % (key, clearText))
            
    except Exception:
        print("An error occurred!")
        traceback.print_exc()

decrypt_cipherText()
