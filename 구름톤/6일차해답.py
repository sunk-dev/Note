# point ]
from itertools import combinations
# ★ 조합구현2: itertools 
blank = [1, 2, 3, 4]
# combinations( 배열, 고를 개수 ) 와 같이 사용합니다.
# combinations 함수의 반환값은 리스트가 아닌 객체이므로 list()를 사용해 변환해주어야 합니다.
comb = list(combinations(blank, 2))
print(comb) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


# 조합구현1: 재귀함수
# 예시로 사용할 공백 배열을 선언할게요. 문자열이 5글자인 경우를 생각하겠습니다. 그럼 공백은 4개겠죠.
blank = [1, 2, 3, 4]

# 조합 결과를 저장할 배열을 선언합니다.
comb = []

# 재귀를 이용한 조합 함수를 만들게요.
# temp는 선택한 공백의 번호를 저장하는 배열입니다.
def combinations(temp, start, end):
	# 만약 temp의 길이가 2이면 모두 고른것이므로 comb에 추가하고 리턴합니다.
	if len(temp) == 2:
		comb.append(temp)
		return

	# 선택한 공백을 추가하고 재귀로 호출합니다.
	for i in range(start, end):
		print(i+1)
		combinations(temp + [blank[i]], i + 1, end)

combinations([], 0, len(blank))
print(comb) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

