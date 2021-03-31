import random 

def get_index(wordlist, letter) :
    pos=0
    index_list =[ ]
    while True :
        try :
            pos = wordlist.index(letter, pos)
            index_list.append(pos)
            pos += 1
        except ValueError :
            break
    return index_list

# Open the file in read mode 

with open("/uploads/sowpods.txt", "r") as file: 

    allText = file.read() 

    words = list(map(str, allText.split())) 

# print random string 
random_word = random.choice(words)
#print (random_word)
    
wordlist=list(random_word)
wordlist_length=len(wordlist)
anslist=[]
print("Hey, Guess the word")
for i in wordlist:
    anslist.append("_")

ans = " ".join(anslist)    
print(ans)    
count=6
while count != 0 :
    letter = input("Say a letter\n")[0]
    print(letter)
    letter=letter.lower()
    occurs = wordlist.count(letter)
    #print (occurs)
    if occurs > 0 :
        wordlist_length -= occurs
        index_list = get_index(wordlist, letter)
        #print(index_list)
        
        for i in index_list:
            anslist[i]=letter
        
        ans = " ".join(anslist)    
        print(ans)      
        print("\n")
        
        if wordlist_length == 0 :
            print("Congratualations !! You have cracked it.")
            break
    else:
        count -=1
        print("Sorry, try again. Lives = " , count , "\n")
else :
    print("Hey, you failed to guess the word. It was \"" + random_word + "\"")