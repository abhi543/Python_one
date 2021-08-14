#largest number from a list
lst=[]
n=int(input("enter the list: "))
for i in range(0, n): 
    ele=int(input())
    lst.append(ele)
print(lst)
def largest_list(lst): 
    max=lst[ 0 ]
    for x in lst: 
        if x>max:
            max=x
        
    return max
print(largest_list(lst))
