def reverseInverse(s):
    result = ""
    tempWord = ""
    nonTempChar = ""
    wordComplete = False
    capsPosInWords = []
    charIndex = 0
    for ch in s:
        if (ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') or (ch in 'abcdefghijklmnopqrstuvwxyz') or (ch in '0123456789') and not wordComplete:
            tempWord = tempWord + ch
            if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                capsPosInWords.append(charIndex)
        else:
            charIndex = 0
            nonTempChar = nonTempChar + ch
            print("Non TempChar"+nonTempChar)
            #print(tempWord)
            
            if len(tempWord) > 0:
                tempWord = (tempWord[::-1]).upper()
                for charPos in capsPosInWords:
                    tempWord = tempWord.replace(tempWord[charPos], chr(ord(tempWord[charPos])+32), 1)
                #print("else templen "+tempWord)
                #print(capsPosInWords)
                result = result + tempWord + nonTempChar
                #print("Result: "+result)
                wordComplete = True
                nonTempChar = ""
                tempWord = ""
                charIndex = 0
                capsPosInWords = []
                continue
            elif ch == ' ':
                wordComplete = False
                charIndex = 0
                print(result)
                result = result + nonTempChar
                nonTempChar = ""
                tempWord = ""
                print("In space")
                continue
            else:
                #result = result + nonTempChar
                nonTempChar = ""
                continue
                    
        charIndex += 1

    #print(result)
    return result

reverseInverse("So, what is CodeFights?")