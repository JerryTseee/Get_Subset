"""
Given a set T of n numbers (represented in an array A[1..n]), a product s,
and one non-negative integer k, our task is to design an algorithm to identify a
subset of numbers in T, with size <= k, such that the product of the numbers 1
in the subset equals s, or report that such a subset does not exist. Design an
algorithm to solve the above problem and analyze the time complexity of your
algorithm.

"""

def findSubset(T, s, k):
    length = len(T)
    for i in range(length):
        for j in range(i, length):
            if (j - i + 1) <= k:
                output = 1
                for p in range(i, j+1):
                    output = output * T[p]
                if output == s:
                    print("found")
                    return
    print("not found")
    return

T = [1,2,3,4,5]
s = 6
k = 3

findSubset(T, s, k)
