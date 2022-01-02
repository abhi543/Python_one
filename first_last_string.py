x=str(input('enter the word'))
if len(x)<6: 
    print("")
else:  
    new_string=x[:3]+x[len(x)-3:]
    print(new_string)