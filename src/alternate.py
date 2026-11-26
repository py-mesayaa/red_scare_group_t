from collections import deque

def alternate(adj_list, red_vertices, s, t):

    if s == t:                                              # to check for the case when s and t are the same vertex 
        return True

    seen = {s} 
    queue = deque([s])

    while queue:                                            #While there are still vertices in the queue

        current = queue.popleft()
        red_vertex = current in red_vertices                #check in red_vertices if the current vertex is red or not

        for neighbour in adj_list[current]:                 #Check all the neighbours of the current vertex
            if neighbour in seen:                           #skip if already visited
                continue
            if (neighbour in red_vertices) == red_vertex:   #Main condition: if current vertex is red, neighbour must be non-red and vice versa
                continue                                    #expression (neighbour in red_vertices) == red_vertex evaluates to True if both are red or both are non-red, which we want to skip
            if neighbour == t:                              #Ends function if we reach t and return True.
                return True
            seen.add(neighbour)
            queue.append(neighbour) 
    return False                                            #once queue is empty and we have not reached t, we return False
