모음=['a', 'e', 'i', 'o', 'u']
word_list=[]
while(True):
    words=input()
    if words=='#':
        break
    else:
        word_list.append(words)

for word in word_list:
    count=0
    for i in word:
        if i.lower()in 모음:
            count+=1
    print(count)
