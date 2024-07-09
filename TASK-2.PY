def maxScore(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints)
    
    remaining_length = n - k
    subarray_sum = sum(cardPoints[:remaining_length])
    
    min_sum = subarray_sum
    
    for i in range(remaining_length, n):
        subarray_sum += cardPoints[i]
        subarray_sum -= cardPoints[i - remaining_length]
        min_sum = min(min_sum, subarray_sum)
    
    return total - min_sum


if __name__ == "__main__":
    cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
    k1 = 3
    print(maxScore(cardPoints1, k1)) 

    cardPoints2 = [2, 2, 2]
    k2 = 2
    print(maxScore(cardPoints2, k2))  
    
    cardPoints3 = [9, 7, 7, 9, 7, 7, 9]
    k3 = 7
    print(maxScore(cardPoints3, k3))
