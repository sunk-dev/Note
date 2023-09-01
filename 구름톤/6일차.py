# 문자열 입력
# for문을 이용해 문자열을 나누는 모든 경우...?
# ex abc
# 20분안에 내가 한것. 3개로 나눌수 있는 모든경우, 중복제거후 사전후 정렬
w=input('문자')
# first 전까지 문자 담고 first에서 Second 까지 문자열 ,Second 이후 문자열
split_words=[]
for first in range(1,len(w)-1):
    for second in range(first,len(w)):
        first_split_word=w[0:first]
        second_split_word=w[first:second+1]
        third_split_word=w[second+1:]
        first_len=len(first_split_word)
        second_len=len(second_split_word)
        third_len=len(third_split_word)
        if(first_len==0 or second_len==0 or third_len==0):
            continue
        split_words.append(first_split_word)
        split_words.append(second_split_word)
        split_words.append(third_split_word)

print(sorted(set(split_words)))

