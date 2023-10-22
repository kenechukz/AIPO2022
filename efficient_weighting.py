"""
Tara Newton received a gift for her birthday. 
In order to guess what’s inside the gift she wants to measure its exact weight. 
Fortunately she has a balance and a set of K weights she can use in her quest. 
Because the weights are in the basement Tara doesn’t want to 
carry more weights than are needed to find the gifts weight.

Your task is to help Tara find out the minimum number of weights she needs 
to carry out of the basement in order to match the weight of her gift.

1st contains the number of weights K.
2nd contains the values for each of the K weights separated by space.
3rd (final) line contains the weight of the gift.

The output is the minimum number of weights needed to match the gifts weight.


"""





def getWeights():
    weightCount = 0
    numOfWeights = int(input())
    weightValues = input().split()
    giftWeight =  int(input())
    total = 0
    found = False
    finalNumOfWeights = 0

    weightValues = [int(item) for item in weightValues]
    weightValues.sort(reverse=True)
    
    finalNumOfWeights = recursion(0,weightValues,total,giftWeight,weightCount,finalNumOfWeights)
    print(finalNumOfWeights)
    
def recursion(i,weightValues,total,giftWeight,weightCount,finalNumOfWeights):

    total += weightValues[i]
    weightCount += 1 

    if total == giftWeight:
        finalNumOfWeights = weightCount
        return finalNumOfWeights

    for j in range(len(weightValues)):
        if total < giftWeight:
            finalNumOfWeights = recursion(j,weightValues,total,giftWeight,weightCount,finalNumOfWeights)
        if finalNumOfWeights > 0:
            break

        if total > giftWeight:
            return 0

        else:
            finalNumOfWeights = -1

    return finalNumOfWeights


getWeights()

"""
Sample Input 1:
3
1 2 5
11

Sample Output 1:
3


Sample Input 2:
1 
2 
5

Sample Output 2:
-1

"""





