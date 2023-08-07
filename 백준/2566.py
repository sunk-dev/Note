#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2566                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jsk2342 <boj.kr/u/jsk2342>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2566                           #+#        #+#      #+#     #
#    Solved: 2023/08/07 14:38:19 by jsk2342       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 2차원 배열 리스트 초기화
matrix=[[0] for _ in range(9)]

for l in range(9):
    low=list(map(int,input().split(' ')))
    matrix[l]=low

max=matrix[0][0]
low=0
colum=0
for l in range(9):
    for c in range(9):
        if matrix[l][c]>max:
            max=matrix[l][c]
            low=l
            colum=c

print(max)
print(f'{low+1} {colum+1}')
