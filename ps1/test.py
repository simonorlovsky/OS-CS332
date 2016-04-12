L = ["ab", "bc", "cd", "de", "ef", "fg", "gh", "hi", "ij", "jh"]
L2 = []
i=0
while (True):
    L2.extend(L)
    i+=1
    if (i%1000000 == 0):
        print i/1000000


