#similarity measures

#pip install packagename

#ex 1 - euclidean distance

import numpy as np
from scipy.spatial import distance

pointA=np.array([2,4,6])
pointB=np.array([5,1,9])

#Euclidean Distance
euclidean_dist=distance.euclidean(pointA, pointB)
print("Euclidean Distance: ", euclidean_dist)

#Similarity(inverse of distance)
similarity_euclidean = 1/(1+euclidean_dist)
print("Euclidean Similarity:", similarity_euclidean)
print()

#ex 2 - 

import numpy as np
from scipy.spatial import distance

pointA=np.array([2,4,6])
pointB=np.array([5,1,9])
manhattan_dist=distance.cityblock(pointA,pointB)
print("Manhattan Distance:", manhattan_dist)

#Similarity(inverse of distance)
similarity_manhattan=1/(1+manhattan_dist)
print("Mahattan Similarity:", similarity_manhattan)

print()

#ex 3 - minkowski

#1. minkowski dist with p=2
minkowski_dist_p3=distance.minkowski(pointA,pointB,p=2)
print("Minkowski Distance(p=3):", minkowski_dist_p3)

#inverse of distance, p=2
similarity_minkowski=1/(1+minkowski_dist_p3)
print("Minkowski similarity(p=2):", similarity_minkowski)

#2. minkowski dist with p=1
minkowski_dist_p3=distance.minkowski(pointA,pointB,p=1)
print("Minkowski Distance(p=1):", minkowski_dist_p3)

#inverse of distance, p=1
similarity_minkowski=1/(1+minkowski_dist_p3)
print("Minkowski similarity(p=1):", similarity_minkowski)

#3. minkowski dist with p=3
minkowski_dist_p3=distance.minkowski(pointA,pointB,p=3)
print("Minkowski Distance(p=3):", minkowski_dist_p3)

#inverse of distance, p=3
similarity_minkowski=1/(1+minkowski_dist_p3)
print("Minkowski similarity(p=3):", similarity_minkowski)

