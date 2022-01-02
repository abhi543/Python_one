subs=200 
likes=5000 
comment=12 

checkers=[
    subs>100,
    likes>1000,
    comment>2
]

if any(checkers): 
    print('awesome video')