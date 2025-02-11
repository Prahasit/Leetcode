class Solution:
    def numTrees(self, n: int) -> int:
        #do recusively  take root and multiply  the no  of trees left and right with their corresponding values
        # if we consider first as node eg node(4) = node(0) * node(3) + node(1) * node(2) + node(2) * node (1) + node (3) * node(0)
        # 0 nodes = 1 tree, 1 node = 1 tree
        numTree = [1] * (n + 1) # initializing array
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]



        