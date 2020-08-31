string_in = input() #inputstring
alp=[] # alphabet character list
oth_index = [] # other character list index
oth=[] # other character list
for i in range(len(string_in)):
    if ord(string_in[i] in range(0, 1)):
        alp.append(string_in[i])
    else:
        oth_index.append(i)
        oth.append(string_in[i])
alp=alp[::-1]#reverse of alphabet
for i in range(len(oth)):
    alp.insert(oth_index[i],oth[i])
print(' '.join(map(str,alp)))