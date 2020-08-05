def writeMessages(messages,method,key):
    f = open("instructions.txt", "a")
    if(method ==1):
        f.write( '00000000'+"\n")
    elif(method == 2):
        f.write( '00000001'+"\n")
        f.write( key+"\n")
    elif(method == 3):
         f.write( '00000003'+"\n")
    for x in messages:
        f.write( x+"\n")
    f.close()
def writeMessages(messages,method):
    f = open("instructions.txt", "a")
    if(method ==1):
        f.write( '00000000'+"\n")
    elif(method == 2):
        f.write( '00000001'+"\n")
        f.write( key+"\n")
    elif(method == 3):
         f.write( '00000003'+"\n")
    for x in messages:
        f.write( x+"\n")
    f.close()

def notEncription(message):
    newMessage = ''
    for x in message:
        x = '1' if (x=='0') else '0'
        newMessage += x
    print(newMessage)
        
def xorEncription(message, key):
    newMessage = ''
    count = 0
    for x in message:
        
        newMessage += str(int(x)^ int(key[count]))
        count+=1
    print(newMessage)
def rotationEncription(message, rotations):
    counter = 0

    while(counter<rotations):
        var = message[len(message)-1]
        message =  message[1:] + var 
        counter+=1
    print(message)

def encription(message, method):
    ASCII_values = [ord(character) for character in message]
    ASCII_hex = []
    for x in ASCII_values:
        var1 =str(hex(int(x)))
        var = var1[2:]
        if(len(var) < 8):
            while(len(var)<8):
                var = '0' + var
            x = var
        ASCII_hex.append(x)

    writeMessages(ASCII_hex, method)
    print(ASCII_hex)
    
