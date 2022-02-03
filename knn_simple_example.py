'''
Suppose Query = (Math=6, comp = 8) and value of k=3

Dataset Given is
Math Comp Result
4      3    Fail
6      7    Pass
7      8    Pass
5      5    Fail
8      8    Pass

So, simply we will find euclidean distance of Query with every Dataset (Math,Comp) and print the result of k nearest value
Here 1,1,2 will be the nearest euclidean distance with Query(math=6,comp=8) and result will be pass

One can simply try this Datatset with different value of k and then can find out why Cross-validation is a required.

Ouput for validating for coodinates math =6 and comp = 8
k = 1, pass
k = 2, pass
k = 3, pass
k = 4, fail
k = 5, fail
k = 6, fail

Since we know that for math =6 and comp = 8 ,  belongs to pass class but after exceeding value of k more than 3
it is giving wrong result, so we can say that for k <= 3 is right for this dataset.

This approach is also called LOOCV(leave One out Cross Validation).
'''
from itertools import count
import math
def euclidean_distance(x,y,qx,qy):
    res = math.sqrt((qx-x)**2 + (qy-y)**2)
    return res

dataset = [[4,6,7,5,8],[3,7,8,5,8],['fail','pass','pass','fail','pass']]
query = [int(x) for x in input("Enter Query :").split(" ")]
k = int(input("Enter Value of K :"))
if((len(dataset[0]) != len(dataset[1])) or (len(dataset[1]) != len(dataset[2]))):
    print("You have wrong Datatset")
lookup = {}
for i in range(len(dataset[0])):
    lookup[i] = euclidean_distance(dataset[0][i],dataset[1][i],query[0],query[1])

lookup = sorted(lookup.items(),key = lambda x:x[1])
result = []
for i,x in enumerate(lookup):
    result.append(dataset[2][x[0]])
    if(i == k-1):
        break

result = sorted(result,key = result.count)
print(f"Query Belongs to Class {result[0]}")



