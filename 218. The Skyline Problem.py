from heapq import heappush, heappop


class Solution(object):
    def getSkyline(self, buildings):
        line=sorted((pos,tag,height,counterpart) for l,r,h in buildings
                    for pos,tag,height,counterpart in [(l,'l',-h,r),(r,'r',-h,l)])
        prev_h,skyline,h_index=0,[],[(0,1<<32)]
        for p,t,h,c in line:
            if t=='l':
                heappush(h_index,(h,c))
            while h_index[0][1]<=p:
                heappop(h_index)
            h,_=h_index[0]
            if h!=prev_h:
                skyline.append((p,-h))
                prev_h=h
        return skyline