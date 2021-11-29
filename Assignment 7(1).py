def DisplayingWordsVowellsConstant ():
    import string
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
    if letters != 0:
        Words+=1
            
        
    print(f"The number of word is {Words}.")


    
    




DisplayingWordsVowellsConstant()