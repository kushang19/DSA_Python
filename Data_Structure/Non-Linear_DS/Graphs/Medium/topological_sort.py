class Solution:
    # Function to perform DFS traversal
    def dfs(self, node, adj, vis, st):
        vis[node] = 1
        
        for it in adj[node]:
            
            if vis[it] == 0:
                self.dfs(it, adj, vis, st)
        
        st.append(node)

    def topoSort(self, V, adj):
        ans = []
        st = []
        vis = [0] * V
        

        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, adj, vis, st)

        while st:
            ans.append(st.pop())

        return ans

if __name__ == "__main__":
    
    V = 6
    adj = [
        [], 
        [], 
        [3], 
        [1], 
        [0, 1], 
        [0, 2]
    ]
    
    sol = Solution()
    
    ans = sol.topoSort(V, adj)
    
    # Output
    print("The topological sorting of the given graph is:")
    for i in range(V):
        print(ans[i], end=" ")