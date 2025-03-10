class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #sort in terms of ages first and then scores
        arr=[]
        len_arr=len(scores)
        sum_scores=sum(scores)
        
        for i in range(len(scores)):
            arr.append([ages[i],scores[i]])
        
        arr.sort()
        
        def helper(ind,prev):
            if ind==len(arr):
                return 0
            
            if (ind,prev) in dp:
                return dp[(ind,prev)]
            
            pick=-math.inf
            
            if prev<=arr[ind][1]:
                pick=arr[ind][1]+helper(ind+1,arr[ind][1])
            
            not_pick=helper(ind+1,prev)
            
            dp[(ind,prev)]=max(pick,not_pick)
            
            return dp[(ind,prev)]
        
        dp={}
        
        return helper(0,0)