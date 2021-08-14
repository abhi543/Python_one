#smallest number from a list
lst=[]
n=int(input("enter the list: "))
for i in range(0, n): 
    ele=int(input())
    lst.append(ele)
print(lst)
def smallest_list(lst): 
    min=lst[ 0 ]
    for x in lst: 
        if x<min:
            min=x
        
    return min
print(smallest_list(lst))