"""
Description of Task:

Calum Watt is a newly hired engineer at a factory. 
His job is to watch the production line and ensure that all products are within an allowed range of error.
You have to help Calum decide if a measurement from the production line falls within the accept- able range or not.


"""




lowerandUpper = str(input('Enter range (x y): ')).split()
L = int(lowerandUpper[0])
U = int(lowerandUpper[1])
M = int(input("Enter number: "))
print(M in range(L,U))




"""
Sample Input 1 
5 9
6
Sample Output 1
True

"""