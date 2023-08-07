#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1316                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jsk2342 <boj.kr/u/jsk2342>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1316                           #+#        #+#      #+#     #
#    Solved: 2023/08/07 16:27:34 by jsk2342       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


count=int(input())
group_word_count=0
words=[]
for w in range(count):
    w=input()
    words.append(w)

# 첫단어는 일단 저장
# 두번째 단어가 첫단어와 같으면 저장x
# 전 단어와 다른 단어오 리스트에도 없으면 저장
# 전단어와 다른 단어인데 리스트에 있으면 그룹단어가 아니므로 False
for word in words:
    bool_group_word=True
    group_word_list=[]
    for i in range(len(word)):
        if i==0:
            group_word_list.append(word[i])
        else:
            if word[i-1]==word[i]:
                continue
            else:
                if word[i] not in group_word_list:
                    group_word_list.append(word[i])
                else:
                    bool_group_word=False
    if bool_group_word:
        group_word_count+=1

print(group_word_count)




