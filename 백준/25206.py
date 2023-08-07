#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25206                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jsk2342 <boj.kr/u/jsk2342>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25206                          #+#        #+#      #+#     #
#    Solved: 2023/08/07 16:31:07 by jsk2342       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 전공 평점 = 전공과목별(학점*과목평점)합 /학점의 총합
#  등급이 P인 과목은 계산에서 제외

# 과목평점 딕셔너리
Subject_rating={
'A+':4.5,
'A0':4.0,
'B+':3.5,
'B0':3.0,
'C+':2.5,
'C0':2.0,
'D+':1.5,
'D0':1.0,
'F':0.0
}

# # 학점의 총합 변수
total_grade=0
# #전공과목별 점수 총합
major_total=0
# #전공 평점 변수
major_rating=0

# # 과목명, 학점, 등급(과목평점으로 변환해야하는)
major_info_list=[]


#  enter_major_info 를 받으면 등급 과목평점으로 변환
# ->전공과목별 점수를 major_total에 저장 
# -> 학점을 total_grade에 저장

#전공 과목 점수 와 학점을 계산하는 함수
def calculate(major_info_list):
    global total_grade
    global major_total
    for major_info in major_info_list:
        if major_info[2]=='P':
            continue
        else:
            total_grade+=float(major_info[1])
            major_total+=float(major_info[1])*change_major_grade(major_info[2])
    return total_grade,major_total


# 등급을 과목평점으로 변환하는 함수
def change_major_grade(grade):
    return Subject_rating[grade]

def clac_major_rating():
    global major_rating
    major_info_list=[]
    for i in range(20):
        enter_major_info=list(input().split(' '))
        major_info_list.append(enter_major_info)
    calculate(major_info_list)
    major_rating=major_total/total_grade
    return major_rating

print(clac_major_rating())

    

