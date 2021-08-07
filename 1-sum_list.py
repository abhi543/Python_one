#sum all the items in a list
lst=[]
n=int(input("enter the list: "))
for i in range(0, n): 
    ele=int(input())
    lst.append(ele)
print(lst)
def sum_list(lst): 
    sum_numbers=0
    for x in lst: 
        sum_numbers +=x
    return sum_numbers
print(sum_list(lst))