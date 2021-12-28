def crowdedGroup(scores, subject, marklimit):
    l = []
    for i in range(len(scores)):
        l.append([])
        for j in range(len(scores)):
            if marklimit >= scores[i][subject] - scores[j][subject] >= 0:
                l[i].append(scores[j]['SeqNo'])
    max = []
    grp=[]
    for i in range(2):
        for k in sorted(l):
            if i==0:
                if len(k) > len(max):
                    max = k
            else:
                if len(max) == len(k):
                    if k in grp:
                        continue
                    else:
                        grp.append(k)

    return grp