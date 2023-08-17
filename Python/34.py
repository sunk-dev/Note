
# .reverse()
li=[1,2,3,4]
li.reverse()

print(li.reverse()) #None반환
print(li) #[4,3,2,1]반환

li2=[1,2,3,4,5]
reversed_li2=list(reversed(li2))
print(li2) # [1,2,3,4,5]반환 값변화 없음
print(reversed_li2) #[5,4,3,2,1]
print(reversed(li2)) # 이터레이터 값 ex)<list_reverseiterator object at 0x00000243DAE3D9C0> 반환