arr = list(input())
frec = [0,0,0,0]
structure = {"A":0, "T":1, "C":2, "G":3}

for i in arr:
    frec[structure[i]]+=1

print(frec)
