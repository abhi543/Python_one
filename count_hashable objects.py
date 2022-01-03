from collections import Counter 

my_list=[11,23,3,2,3,3,3,2,7,6,5,6,7,6]
counter=Counter(my_list)

print(counter)

most_common=counter.most_common(1)
print(most_common)