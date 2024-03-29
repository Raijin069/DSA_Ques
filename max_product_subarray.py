def max_product_subarray(A):
    curr_min = A[0]
    curr_max = A[0]
    prev_max = A[0]
    prev_min = A[0]
    result = A[0]

    for i in range(1,len(A)):
        curr_max = max(prev_max*A[i],prev_min*A[i],A[i])
        curr_min = min(prev_max*A[i],prev_min*A[i],A[i])
        result = max(curr_max,result)
        prev_max = curr_max
        prev_min = curr_min
    return result

        