lst=[]
n=int(input("enter the list: "))
for i in range(0, n): 
    ele=int(input())
    lst.append(ele)
print(lst)
def multiply_list(lst): 
    numbers=1
    for x in lst: 
        numbers *=x
    return numbers
print(multiply_list(lst))