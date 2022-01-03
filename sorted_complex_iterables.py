data=(2,6,4,12)
sorted_data=sorted(data,reverse=True)
print(sorted_data)

data1=[{"name":"Max","age":6},
       {"name":"Lisa","age":20},
       {"name":"herra", "age":3}]
sorted_data=sorted(data1,key=lambda x:x["age"])
print(sorted_data)