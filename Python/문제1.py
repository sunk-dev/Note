import random as r
computer_turn_num=r.randint(1,3)

# 최대 3개를 받았는지를 검사하는 함수
def check_count(li,human_start_num):
    if(len(li)>3 or li[0]!=human_start_num+1):
        print('입력 개수를 초과했거나 컴퓨터가 외친 마지막 숫자보다 작은 숫자부터 입력했습니다. 입력은 최대 3개까지 이고 컴퓨터가 외친 다음 번호부터 입력하세요.')
        return;

human_start_num=1
# 인간하고 컴퓨터가 외친 총 숫자를 담을 리스트

while (True):
        my=list(map(int,input("My turn-숫자를 입력하세요:").split(' ')))
        check_count(my,human_start_num)
        # 내가 31을 입력했는지 체크
        if my[-1]==31:
            print('게임끝 ! 컴퓨터 승리! ')
            break
        # 컴퓨터가 뱉기 시작할 숫자
        computer_start_num=my[-1]
        # print(computer_start_num)
        # 컴퓨터가 몇개를 뱉을지를 정하는 변수
        computer_turn_num=r.randint(1,3)
        for i in range(computer_turn_num):
            computer_start_num+=1
            print(computer_start_num,end=' ')
            if computer_start_num==31:
                break
        print()
        if computer_start_num==31:
            print('게임끝 ! 인간 승리! ')
            break
        
        human_start_num=computer_start_num+1






