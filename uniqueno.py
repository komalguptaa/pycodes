def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
        return x
print(unique_list([6,9,6,9,4,7,99,78,2]))