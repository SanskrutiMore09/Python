# this has a bug 
i=0
while i < 10 :
    if i == 5 :
        continue
    print(i)
    i+=1

# solution
i=0
while i < 10 :
    if i == 5 :
        i+=1
        continue
    print(i)
    i+=1
