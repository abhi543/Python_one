#a Python function to create the HTML string with tags around the wordS
def add_tags(tag,word): 
    return "<%s><%s><%s>" % (tag,word,tag) 
print(add_tags('i','hero'))