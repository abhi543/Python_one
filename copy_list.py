lst=[]
n=int(input("enter the list: "))
for i in range(0, n): 
    ele=int(input())
    lst.append(ele)
print(lst)
one=lst.copy()
print('copied list: ',one)