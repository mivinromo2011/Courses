import sys
class Network():
    def __init__(self, vertices):
        self.V = vertices
        self.network = [[0 for column in range(vertices)]
                    for row in range(vertices)]
    def printMST(self, parent):
        s=0
        for i in range(1, self.V):
            s+=self.network[i][parent[i]]
        return s
    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index=-1
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        flag=True
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            if u==-1:
                flag=False
                break
            mstSet[u] = True
            for v in range(self.V):
                if self.network[u][v] > 0 and mstSet[v] == False and key[v] > self.network[u][v]:
                        key[v] = self.network[u][v]
                        parent[v] = u
        if flag:
            return self.printMST(parent)
        else:
            return -1

k=int(input())
while k>0:
    n,m=map(int,input().split())
    edges=[]
    for i in range(m):
        u,v,c=map(int,input().split())
        edges.append([u-1,v-1,c])
    s=[]
    g=Network(n)
    p=[[0 for k in range(n)]for j in range(n)]
    for j in range(m):
        p[edges[j][0]][edges[j][1]]=edges[j][2]
        p[edges[j][1]][edges[j][0]]=edges[j][2]
    g.network=p
    mst=g.primMST()
    if mst!=-1:
        s.append(mst)
    for i in range(m):
        g = Network(n)
        p=[[0 for k in range(n)]for j in range(n)]
        for j in range(m):
            if j!=i:
                p[edges[j][0]][edges[j][1]]=edges[j][2]
                p[edges[j][1]][edges[j][0]]=edges[j][2]
        g.network=p
        mst=g.primMST()
        if mst!=-1:
            s.append(mst)
    if len(s)==0:
        print("No way")
    elif len(s)==1:
        print("No second way")
    else:
        s.sort()
        print(s[1])
    k-=1
