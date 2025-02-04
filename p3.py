def count_subarrays_with_sum(arr, sum):
    current_sum = 0
    count = 0
    sub_sum_count = {0: 1}
    
    for n in arr:
        current_sum += n
        if (current_sum - sum) in sub_sum_count:
            count += sub_sum_count[current_sum - sum]
        if current_sum in sub_sum_count:
            sub_sum_count[current_sum] += 1
        else:
            sub_sum_count[current_sum] = 1
    
    return count

print(count_subarrays_with_sum([1, 2, 3, 4, 5], 9))
