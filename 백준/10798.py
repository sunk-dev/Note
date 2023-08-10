#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10798                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jsk2342 <boj.kr/u/jsk2342>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10798                          #+#        #+#      #+#     #
#    Solved: 2023/08/10 15:33:29 by jsk2342       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


word_list=[[0]*1 for _ in range(5)]
max_len=0
sentence=''

for i in range(5):
    word=list(input())
    word_list[i]=word
    if(max_len<len(word)):
        max_len=len(word)

for c in range(max_len):
    for r in range(5):
        try:
            sentence+=word_list[r][c]
        except:
            sentence+=''
print(sentence)         


