def listToString(list):  
        
    newString = ""  
        
    for element in list:  
        newString += element   
        
    return newString

def stringToList(string):
    newList = [] 
    
    for element in string:
        newList.append(element)
    
    return newList

def encode(rot, sentence):
    

    abc = 'abcdefghijklmnopqrstuvwxyz'
    encodedSentence = []

    for i in range(len(sentence)):
        if sentence[i] != ' ':
            letter = abc.index(sentence[i].lower())
            loop = 0

            while loop < rot:
                if letter > len(abc) - 1:
                    letter = 0
                letter = letter + 1
                loop = loop + 1
            if letter > len(abc) - 1:
                    letter = 0

            encodedSentence.append(abc[letter])
        
        else:
            encodedSentence.append(' ')
    return encodedSentence

string = input("What text do you want to encode? ")
rot = int(input("What number do you want to be the rot to encode with? "))
encodedString = listToString(encode(rot, string))

print(encodedString)

saveToFile = input("Do you want to save this message to a file? |Y| |N| ").lower()
if saveToFile == 'y':
    f = open('message.txt', 'w')
    f.write(encodedString)
