"""
Description:

We are given a simple word search to solve, 
where there is only one word we are looking to find -“AIPO”
The grid we are searching in is not necessarily square, 
and you can find the word “AIPO” in 3 possible directions - vertically, horizontally, and diagonally

The first line consists of two numbers N and M representing the width and height of the grid to search.
N lines follow, each containing M characters. This forms the grid to search.



"""






def search(searchWord,grid,curRow,curCol,visited):
    # Check if cell has been visited
    coordKey = str(curRow) + "-" + str(curCol)
    if str(curRow) + "-" + str(curCol) in visited:
        return
    
    visited.add(coordKey)

    #Check top boundary
    if curRow < 0:
        return

    #check right boundary
    if curCol >= cols:
        return

    #check bottom boudary
    if curRow >= rows:
        return

    #check left boundary
    if curCol < 0:
        return
    
    
    
    # Top
    search(searchWord,grid,curRow-1,curCol,visited)

    # Top right
    search(searchWord,grid,curRow-1,curCol+1,visited)

    # Right
    search(searchWord,grid,curRow,curCol+1,visited)

    # Bottom right
    search(searchWord,grid,curRow+1,curCol+1,visited)

    # Bottom
    search(searchWord,grid,curRow+1,curCol,visited)

    # Bottom left
    search(searchWord,grid,curRow+1,curCol-1,visited)

    # Left
    search(searchWord,grid,curRow,curCol-1,visited)

    # Top left
    search(searchWord,grid,curRow-1,curCol-1,visited)

    #print(grid[curRow][curCol])
    findWordInCell(searchWord,0,"top",grid,curRow,curCol)
    findWordInCell(searchWord,0,"topright",grid,curRow,curCol)
    findWordInCell(searchWord,0,"right",grid,curRow,curCol)
    findWordInCell(searchWord,0,"bottomright",grid,curRow,curCol)
    findWordInCell(searchWord,0,"bottom",grid,curRow,curCol)
    findWordInCell(searchWord,0,"bottomleft",grid,curRow,curCol)
    findWordInCell(searchWord,0,"left",grid,curRow,curCol)
    findWordInCell(searchWord,0,"topleft",grid,curRow,curCol)

    return


def findWordInCell(word,wordIndex,direction,grid,curRow,curCol):
    
    #Check top boundary
    if curRow < 0:
        return 0

    #check right boundary
    if curCol >= cols:
        return 0

    #check bottom boudary
    if curRow >= rows:
        return 0

    #check left boundary
    if curCol < 0:
        return 0

    #checking that it has not gone past the word    
    if wordIndex > len(word)-1: 
        return 0

    #check that the current letter in cell is equal to the letter in the word's index
    if grid[curRow][curCol].lower() != word[wordIndex].lower():
        return 0

    if (grid[curRow][curCol].lower() == word[wordIndex].lower()) and wordIndex == len(word)-1: 
        #print(grid[curRow][curCol])
        #print("row is ",curRow)
        #print("col is ",curCol)
        #print('we found it at ',direction) 
        if 'count' not in globals():
            global count
        globals()['count'] += 1
        return 1

    #print(grid[curRow][curCol])
        
    if direction == "top":
        # Top
        return findWordInCell(word,wordIndex+1,"top",grid,curRow-1,curCol)
    
    if direction == "topright":
        # Top right
        return findWordInCell(word,wordIndex+1,"topright",grid,curRow-1,curCol+1)

    if direction == "right":
        # Right
        return findWordInCell(word,wordIndex+1,"right",grid,curRow,curCol+1)
        
    if direction == "bottomright":
        # Bottom right
        return findWordInCell(word,wordIndex+1,"bottomright",grid,curRow+1,curCol+1)
        
    if direction == "bottom":
        # Bottom
        return findWordInCell(word,wordIndex+1,"bottom",grid,curRow+1,curCol)
        
    if direction == "bottomleft":
        # Bottom left
        return findWordInCell(word,wordIndex+1,"bottomleft",grid,curRow+1,curCol-1)
        
    if direction == "left":
        # Left
        return findWordInCell(word,wordIndex+1,"left",grid,curRow,curCol-1)
           
    if direction == "topleft":
        # Top left
        return findWordInCell(word,wordIndex+1,"topleft",grid,curRow-1,curCol-1)
            


grid = []

err = False

widthAndHeight = input().strip()


if widthAndHeight != '':

    widthAndHeight = widthAndHeight.split()

    if len(widthAndHeight) > 1 and widthAndHeight[0].isnumeric() and widthAndHeight[1].isnumeric():

        rows = int(widthAndHeight[0])

        cols = int(widthAndHeight[1])
    else:
        err = True
else:
    err = True




if err == False:
    if rows not in range(4,2501) or cols not in range(4,2501):
        err = True
    else:
        for row in range(rows):
            rowStr = input().strip()
            while len(rowStr) < cols:
                rowStr += ' ' 
            if len(rowStr) not in range(4,2501):
                err = True
                break
            grid.append(rowStr)

     






searchWord = 'aipo'


visited = set()

count = 0

if err == False:
    search(searchWord,grid,0,0,visited)
    print(f"\n{globals()['count']}")

# Test cases
"""
All spaces: Passed
4 4






Special chars: Passed
4 4
€§∞•
¡ªº•
•¶¡“
•¶¡“

Special chars for weight and height: Passed
∞ º
wedsa
wenao
froms
frpqw



"""


"""
Sample Input 1
9 11
UQTTZTYBSOW
AOCEUPCOPIA
IPOAIPOPIAU
PIPNHZQNSMO
OAURQOPIAPA
AIPOOMIIIAI
AIVRRPPAIIP
RTPQAOIPKPO
ABROWMOAEOA

Sample Output 1
14


Sample Input 2
4 4
aipo
iiii
pppp
oooo

Sample Output 2
3



"""