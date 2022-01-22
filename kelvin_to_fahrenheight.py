import sys
def kel(temp): 
    assert(temp>=0),"colder than absolute temperature"
    return((temp-273)*1.8)+32

print(kel(273))
print(sys.getsizeof(kel))