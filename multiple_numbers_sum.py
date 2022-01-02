def sum(*a): 
    result=0 
    for i in a: 
        result=result +i 
    return result 

res=sum(2,3,4,5)
print(res)