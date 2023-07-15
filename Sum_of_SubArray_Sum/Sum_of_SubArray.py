#You are given an integer array A of length N.
#You have to find the sum of all subarray sums of A.
#PS: A subarray sum denotes the sum of all the elements of that subarray.
#Input    A = [1, 2, 3]
#Output    20


def sumofSubArray(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    for i in range(len(array)-1):
        sum+=array[i]+array[i+1]
    for i in range(len(array)-2):
        sum+=array[i]+array[i+1]+array[i+2]
    return sum

array=[1,2,3]
print(sumofSubArray(array))