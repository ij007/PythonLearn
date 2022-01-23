class Queue:
    queue= list()
    def init(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    
    def isempty(self):
        return(self.queue == [])

    def str(self):
        return(str(self.queue))

def longestpathlist(AList):
    (indegree,lpath) = ({},{})
    zerodegreeq = Queue()

    for u in AList.keys():
        (indegree[u],lpath[u]) = (0,0)
    
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)
                
    while (not zerodegreeq.isempty()):
        j = zerodegreeq.delq()
        indegree[j] = indegree[j]-1
        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            lpath[k] = max(lpath[k],lpath[j]+1)
            if indegree[k] == 0:
                zerodegreeq.addq(k)
    return lpath

def longJourney(AList):
    lpathdict = longestpathlist(AList)
    ind = max(lpathdict.values())
    lpathlist = []
    while ind != -1: 
        if lpathlist == []:
            for i in lpathdict:
                if lpathdict[i] == ind:
                    lpathlist.insert(0,i)
        else:
            for i in lpathdict:
                if lpathdict[i] == ind and (lpathlist[0] in AList[i]):
                    lpathlist.insert(0,i)
                else:
                    pass
        ind = ind - 1
    return lpathlist