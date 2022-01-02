subs=200 
likes=5000 
comment=12 

conditions=[
    subs>100,
    likes>1000,
    comment>2
]

if all(conditions): 
    print('awesome video')