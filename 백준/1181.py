word_num=int(input('단어개수입력'))
word_list=[]
for i in range(word_num):
    word=input('단어입력')
    word_list.append(word)

#중복제거
word_list=list(set(word_list))
endIndex=len(word_list)
# new_word_list=[]
# new_word_list.append(word_list[0])
for i in range (endIndex):
    fnum=word_list[i] #움직이는 단어
    for j in range(0,endIndex):
        if len(fnum)




    # for j in range(len(new_word_list)):
    #     if len(enterword)<len(new_word_list[j]):
    #         new_word_list.insert(j-1,enterword)
    #     elif len(enterword)==len(new_word_list[j]):
    #         if enterword>new_word_list[j]:
    #             new_word_list.insert(j+1,enterword)
    #         else:
    #             new_word_list.insert(j-1,enterword)
    #     else:
    #         new_word_list.append(enterword)



print(new_word_list)

