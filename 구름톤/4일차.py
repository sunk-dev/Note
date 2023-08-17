ingredient_count=int(input())
ingredient_list=list(map(int,input().split(' ')))
max_flavor=max(ingredient_list)
max_flavor_index=ingredient_list.index(max_flavor)
is_valid=True
for i in range(1,max_flavor_index):
    if ingredient_list[i-1]>max_flavor or ingredient_list[i-1]>ingredient_list[i]:
        is_valid=False
for i in range(max_flavor_index+1,len(ingredient_list)):
    if ingredient_list[i-1]>max_flavor or ingredient_list[i-1]<ingredient_list[i]:
        is_valid=False
if (is_valid==False):
    print(0)
else:
    print(sum(ingredient_list))
