
#Caesar ciper

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")
    
    # Get the message to encode
    message = input("Please enter the message to encode: ")

    print("\nEncoded:")
    encodedMessage = encode(message)
    print(encodedMessage)
    
    decodedMessage = decode(encodedMessage)
    print("\nDecoded:")
    print(decodedMessage)

def encode(message):
    # Loop through the message and print out the Unicode values
    chList =[]
    for ch in message.upper():
        if(' ' == ch or '!' == ch):
            chList.append('!')
        else:
            index = (ord(ch) - ord('A')+1) % 26
            #print("\nIndex:", index)
            chList.append(chr(ord('A')+ index))

    return ''.join(chList)


def decode(message):
    # Loop through the message and print out the Unicode values
    chList =[]
    for ch in message.upper():
        if('!' == ch):
            chList.append(' ')
        else:
            index = abs(ord(ch) - ord('Z')-1) % 26
            #print("\nIndex:", index)
            chList.append(chr(ord('Z')- index))

    return ''.join(chList)
main()
