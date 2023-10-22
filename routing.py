"""
You have been tasked with managing a network of N computers. 
Every computer on the networkis numbered between 1 and N and is connected with cables to some other computer on the same
network - each computer is guaranteed to be connected to one or more other computers.

When a computer wants to communicate with another computer, the message may have to travel
through other computers in the network to reach its destination. Every cable between computers
has a unique latency - a time delay between the computers at each end. When a message leaves one
computer, it takes this time to reach the other computer at the other end of the cable. 

Assume all messages between computers travel with the minimum possible latency, if there are multiple possible
routes.
For the example below, if a message needs to travel from computer 2 to computer 5, the minimum
latency is 1 + 2 + 4 + 5 = 12 ms following route 2,1,6,3,5.


Your task is, given a network of computers and cables, find the two computers on the network,
which have the largest latency between them, even when the lowest latency route between them is
taken. For the above example, the answer is computers 4 and 5, which have latency 15ms between
them.


Input/Output:
1st line  contains two integers, N (number of computers) and M (number of cables in network), 
The following M lines describe cables joining pairs of computers on the network.
Each containthree values a, b and l - the numbers of the computers connected by the cable, and the latency of the
cable in milliseconds.

The output: the numbers of the computers that have the maximum latency (in increasing order), and their latency


"""





def maxDijkstra(adjnodes,compCnt,mainSourceComp):
  distances = [0 for _ in range(0,compCnt)]
  distances[mainSourceComp-1] = 0
  visited = set()
  lastComp = -1
  maxDist = -1
  maxSrc = -1
  maxDest = -1
  # mainSourceComp is called seven times, each iteration representing a computer
  srcComp = mainSourceComp

  
  while lastComp != srcComp:# and adjnodes.get(srcComp):
    #print("before: ")
    #print(distances)
    # The previous source computer gets assigned to lastComp and srcComp then gets update
    lastComp = srcComp
    srcComp = updateSourceNodeCost(adjnodes,srcComp,visited,distances,mainSourceComp)
    # srcComp-1 brings computer into correspond index example: [0,0,0,0,0,0,0] and the srcComp is 5:[0,0,0,0,(5's cost) 0,0,0]
#0 1 2 3 4 5 6                        0 1 2 3   4          5 6
 # Comp:                              1 2 3 4   5          6 7     
 # MaxSrc represents overall source computer   
    if distances[srcComp-1] > maxDist:
      maxDist = distances[srcComp-1]
      maxSrc = mainSourceComp
      maxDest = srcComp

  return [maxSrc,maxDest,maxDist]


def updateSourceNodeCost(adjnodes,srcComp,visited,distances,mainSourceComp):
  maxComp = srcComp
  
# Step 1: Am I connected to any nodes? -> Check adjacency nodes
  for conn in adjnodes[srcComp]:
# Step 2: Have we visited this computer before 
    if conn not in visited:#srcComp not in visited
      #print(str(srcComp) + "->" + str(conn) + ": " + str(adjnodes[srcComp][conn]))
      cost = adjnodes[srcComp][conn] + distances[srcComp-1]
      if(cost > distances[conn-1]):
        distances[conn-1] = cost
# Step 3: Is the cost of the computer we're connecting to greater than the cost of the current computer? -> If true make it the current source comp and add last source computer to visited, otherwise don't change it 
        if distances[conn-1] > distances[maxComp-1]:
          maxComp = conn
          
          
  visited.add(srcComp)
  srcComp = maxComp
  

  


  #print("after: ")
  #print(distances)
  return srcComp


def minDijkstra(adjnodes,maxSrc,maxDest):
#minDijkstra(maxSrc,maxDest,adjnodes,visited):
  visited = set()
  srcComp = maxSrc
  distances = [2147483647 for _ in range(0,compCnt)]
  distances[maxSrc-1] = 0
  
  lastSrcComp = -1
  while srcComp != maxDest and srcComp != lastSrcComp:
    minCost = 2147483647
    minComp = srcComp
    if adjnodes.get(srcComp):
  # Step 1: Am I connected to any nodes? -> Check adjacency nodes
      for conn in adjnodes[srcComp]:
    # Step 2: Have we visited this computer before, calculate the cost of the node 
        if srcComp not in visited:
          cost = distances[srcComp-1] + adjnodes[srcComp][conn]
          if(cost < distances[conn-1]):
            distances[conn-1] = cost
    # Step 3: Is the cost of the computer we're connecting to less than the cost of the current computer? -> If true make it the current source comp and add last source computer to visited, otherwise don't change it 
            if distances[conn-1] < minCost:
              minCost = distances[conn-1]
              minComp = conn

      lastSrcComp = srcComp
      visited.add(srcComp)
      srcComp = minComp
      result = str(maxSrc),str(maxDest),str(distances[maxDest-1])
    
  return ' '.join(result)
    
  
  
  
  
  


'''
*************** The program starts here ********************** 
'''

cAndC = input()
cAndC = cAndC.split()
cAndC = [int(i) for i in cAndC]
compCnt = cAndC[0]
cables = cAndC[1]
conn = []
adjnodes = dict()
pairLatency = {}
maxLatency = 0
compList = [0 for _ in range(0,compCnt)]

userEntry = [input() for i in range(cables)]

network = {}






for i in range(cables):
  conn = userEntry[i].split() 
  conn0 = int(conn[0])
  conn1 = int(conn[1])
  conn2 = int(conn[2])


  compList[conn0-1] = conn0
  compList[conn1-1] = conn1

  
  #building the adjacency list
  if not adjnodes.get(conn0):
    adjnodes[conn0] = dict()
  adjnodes[conn0][conn1] = conn2

  #building the adjacency list
  if not adjnodes.get(conn1):
    adjnodes[conn1] = dict()
  adjnodes[conn1][conn0] = conn2
  
  
maxLatency = 0
maxSrc = -1
maxDest = -1


for i in compList:
  dijkstraReturn = maxDijkstra(adjnodes,compCnt,i)
  
  

  if dijkstraReturn[2] > maxLatency:
    maxLatency = dijkstraReturn[2]
    maxSrc = dijkstraReturn[0]
    maxDest = dijkstraReturn[1]


  

print(minDijkstra(adjnodes,maxSrc,maxDest))



"""
Sample Input 1
7 7
5 3 5
3 6 4
6 1 2
3 1 8
1 7 6
2 1 1
2 4 3

Sample Output 1
5 7 17




"""