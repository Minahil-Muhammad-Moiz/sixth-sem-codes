def conversion(task, text, key):
    convertedText = ""
    for char in text:      
        match task:
            case "e":
                convertedText +=chr((ord(char)-97 + ord(key[i])-97) % 26 +97)
            case 'd':
                convertedText +=chr((ord(char) - ord(key[i]) + 26) % 26 +97)
    
    print(convertedText)   

while True:
    task = input("Type 'e' for Encryption and 'd' for Decryption: ").lower()
    text = ''.join(input("Enter PlainText: ").lower().split())
    key = ''.join(input("Enter Key: ").lower().split())

    paddedKey = ''
    for i in range(len(text)):
        paddedKey+=key[i%len(key)]

    conversion(task, text, paddedKey)

    runAgain = input("Type 'y' for Again and 'n' for Ending: ").lower()
    if runAgain == 'n':
        print('Program Ends!')
        break