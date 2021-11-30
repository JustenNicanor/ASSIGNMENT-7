def DisplayingWordsVowellsConstant ():
    letters=0
    Words=0
    Vowells=0
    Consonants=0
    Sentence = input("Give a sentence: ")
    sentencelength = len(Sentence)
    for i in range(sentencelength):
        if Sentence[i] ==" " :
            if letters != 0:
                Words+=1
        else:
            letters+=1
            if Sentence[i] == "A" or Sentence[i] == "a":        
                Vowells+=1
            elif Sentence[i] == "E" or Sentence[i] == "e":
                Vowells+=1
            elif Sentence[i] == "I" or Sentence[i] == "i":
                Vowells+=1
            elif Sentence[i] == "O" or Sentence[i] == "o":
                Vowells+=1
            elif Sentence[i] == "U" or Sentence[i] == "u":  
                Vowells+=1
            else:
                Consonants+=1
    if letters != 0:
        Words+=1
    
    
    print(f"WORDS: {Words}")
    print(f"VOWELLS: {Vowells}")
    print(f"CONSONANTS: {Consonants}")
    




DisplayingWordsVowellsConstant()
