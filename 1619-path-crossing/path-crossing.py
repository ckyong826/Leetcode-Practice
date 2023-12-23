class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathMap=defaultdict(int)
        plane=[0,0]
        pathMap[tuple(plane)]+=1
        for i in path:
            if i=='N':
                plane[1]+=1
            elif i=='S':
                plane[1]-=1
            elif i=='E':
                plane[0]+=1
            else:
                plane[0]-=1
            pathMap[tuple(plane)]+=1
        return any(pathMap[j] > 1 for j in pathMap)

