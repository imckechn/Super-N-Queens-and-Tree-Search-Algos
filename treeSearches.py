from helpers import graphInit, getWeight, getHeuristic

# Breadth First Search
# @Params
# Graph is the list of graph nodes
# current is the current element
# End is the node that's is the end of the graph
# Visted are the nodes that have been visited already
# Returns a string indicating the path found
def depthFirst(graph, current,  end, visited):
    if current == end:
        return end

    for elem in graph:

        #This checks if we've visited the node already, this way we wont go into a cycle
        if elem in visited:
            continue

        #If the element is the node we are on
        if elem[0] == current:

            #Call DFS on the found node
            visited.append(elem)
            ans = depthFirst(graph, elem[2], end, visited)

            #If not found keeping looping
            if ans == None:
                visited.pop()
                continue

            else: #return the string with the current node on it
                return elem[2] + "-" + ans

    #When there is no nodes left, return None
    return None


# Depth First Search
# @Params
# Graph is the list of graph nodes
# current is the current element
# End is the node that's is the end of the graph
# Visted are the nodes that have been visited already
# Returns a string indicating the path found
def breadthFirst(graph, current,  end, visited):

    answer = ""
    queue = []
    queue.append(current)

    while len(queue) > 0:
        v = queue.pop(0)
        answer += v+"-"

        if v == end:
            answer = answer[:-1] #Remove the last dash
            return answer

        for elem in graph:

            if elem[0] == v and elem[2] not in visited:

                queue.append(elem[2])
                visited.append(elem[2])

    #When there is no nodes left, return None
    return None

# Uniform Cost Search
# @Params
# Graph is the list of graph nodes
# current is the current element
# End is the node that's is the end of the graph
# Visted are the nodes that have been visited already
# Returns a string indicating the path found
def uniformCost(graph, current,  end, visited):
    if current == end:
        return end

    options = []

    for elem in graph:

        #This checks if we've visited the node already, this way we wont go into a cycle
        if elem in visited:
            continue

        #If the element is the node we are on
        if elem[0] == current:
            options.append(elem)

    #sort the options by smallest cost
    options.sort(key=getWeight)

    for elem in options:
        #Call DFS on the found node
        visited.append(elem)
        ans = uniformCost(graph, elem[2], end, visited)

        #If not found keeping looping
        if ans == None:
            visited.pop()
            continue

        else: #return the string with the current node on it
            return elem[0] + "-" + ans


    #When there is no nodes left, return None
    return None


# Greedy Best First
# @Params
# Graph is the list of graph nodes
# current is the current element
# End is the node that's is the end of the graph
# Visted are the nodes that have been visited already
# Returns a string indicating the path found
def greedyBestFirst(graph, current,  end, visited):
    if current == end:
        return end

    options = []

    for elem in graph:

        #This checks if we've visited the node already, this way we wont go into a cycle
        if elem in visited:
            continue

        #If the element is the node we are on
        if elem[0] == current:
            options.append(elem)

    #sort the options by smallest cost
    options.sort(key=getHeuristic)

    for elem in options:
        #Call DFS on the found node
        visited.append(elem)
        ans = greedyBestFirst(graph, elem[2], end, visited)

        #If not found keeping looping
        if ans == None:
            visited.pop()
            continue

        else: #return the string with the current node on it
            return elem[0] + "-" + ans

    #When there is no nodes left, return None
    return None


def aStarHelper(element):
    return element[1] + element[3]


def aStar(graph, current, end, visited):
    if current == end:
        return end

    if len(visited) == len(graph):
        return None

    options = []

    #Add the children to the options
    for elem in graph:
        if elem[0] == current and elem not in visited:
            options.append(elem)

    #Sort the array by smallest heuristic + distance
    options.sort(key=aStarHelper)

    #Loop through the options
    for elem in options:
        visited.append(elem)

        ans = aStar(graph, elem[2], end, visited)
        if ans == None:
            continue
        else:
            return elem[0] + "-" + ans


graph = graphInit()

print("Depth First Search")
dfs = depthFirst(graph, "S", "F", [])
if dfs:
    print('S-' + dfs)
else:
    print("No Solution")



print("Breadth First Search")
bfs = breadthFirst(graph, "S", "F", [graph[0]])
if bfs:
    print(bfs)
else:
    print("No Solution")



print("Uniform cost search")
ucs = uniformCost(graph, "S", "F", [graph[0]])
if ucs:
    print(ucs)
else:
    print("No Solution")



print("Greedy Best-First Searhc")
gbf = greedyBestFirst(graph, "S", "F", [graph[0]])
if gbf:
    print(gbf)
else:
    print("No Solution")



print("A* Search")
aStar = aStar(graph, "S", "F", [])
if aStar:
    print(aStar)
else:
    print("No Solution")