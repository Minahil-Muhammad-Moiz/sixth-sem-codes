alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def conversion(task, text, shiftKey):
    convertedText = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            match task:
                case "e":
                    newPosition = (position + shiftKey)%26
                case 'd':
                    newPosition = (position - shiftKey)%26

            convertedText += alphabet[newPosition]
        else:
            convertedText += char
    
    print(convertedText)   

while True:
    task = input("Type 'e' for Encryption and 'd' for Decryption: ").lower()
    text = input('Type your Message \n').lower()

    conversion(task, text, 6)

    runAgain = input("Type 'y' for Again and 'n' for Ending: ").lower()
    if runAgain == 'n':
        print('Program Ends!')
        break