class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #start from 0 as it's unlocked
        def dfs(node):
            visit.add(node)
            for nei in rooms[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)


        visit = set()
        dfs(0)
        #now we need to check if all the rooms are there in visit. if not then one or more rooms is unreacheable so cannot be unlocked to FALSE
        return len(rooms) == len(visit)
