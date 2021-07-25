def And(a,b): 
    if a==True and b==True:
        return 'true'
    elif a==True and b==False:
        return 'False'
    elif a==False and b==True: 
        return 'False'
    elif a==False and b==False:
        return 'False'
        
print(And(True,True))
            
        
