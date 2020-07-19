#chooses the sentence from a block of text that best summarizes it
from collections import Counter
import re

txt=input("Paste the block of text you would like to summarize: ")

wordlist=txt.split(" ")

wc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","'","&"]

for i in range(0,len(wordlist)-1):
    wordlist[i]=wordlist[i].lower()
    for j in range(0,len(wordlist[i])-1):
        if wordlist[i][j] not in wc:
            wordlist[i]=wordlist[i].replace(wordlist[i][j]," ")
            
c=Counter(wordlist).most_common();

#converts tuple c to list c2 with weighted frequencies
c2=[] #words with their weighted frequencies
ctemp=[]
hfreq = c[0][1]
for k in range(len(c)):
    wefreq=c[k][1]/hfreq
    ctemp=list(c[k])
    ctemp[1]=wefreq
    c2+=ctemp

temp2=0
#split text by sentences
bysent=re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',txt)
bysen2=re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',txt)
wfs=[]

punc=[".","?","!"]

for l in range(len(bysent)):
    bysent[l]=bysent[l].lower()
    temp2=bysent[l].split(" ")

    for i in range(len(temp2)):
        for j in range(0,len(temp2[i])-1):
            if temp2[i][j-1] in punc:
                temp2[i]=temp2[i].replace(temp2[i][j-1],"")
     
    d=Counter(temp2).most_common();
    temp3=0
    temp4=0
    for i in range(len(d)):
        for o in range(len(c2)):
            if d[i][0]==c2[o]:
                temp3=d[i][1]*c2[o+1]
                temp4+=temp3

    wfs.append(temp4)

sumnum=wfs.index(max(wfs))
summary=bysen2[sumnum]

print()
print("The sentence that summarizes your text:\n"+summary)
