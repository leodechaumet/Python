def topologicalSortUtil(graphe,v,visited,stack): 

    # Mark the current node as visited. 
    visited[v] = True

    # Recur for all the vertices adjacent to this vertex 
    for i in graphe.neighbors(v): 
        if visited[i] == False: 
            topologicalSortUtil(graphe, i,visited,stack) 

    # Push current vertex to stack which stores result 
    stack.insert(0,v) 

    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
def topologicalSort(graphe): 
    # Mark all the vertices as not visited 
    visited = dict(zip(g.vertices(),[False]*graphe.n()))
    stack =[] 

    # Call the recursive helper function to store Topological 
    # Sort starting from all vertices one by one 
    for v in graphe.vertices(): 
        if visited[v] == False: 
            topologicalSortUtil(graphe,v,visited,stack) 

    # Print contents of stack 
    print(stack)
