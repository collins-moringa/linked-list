def count_positives_sum_negatives(arr):
    if not arr:
        return []

    positive_count = sum(1 for n in arr if n > 0)
    negative_sum = sum(n for n in arr if n < 0)

    return [positive_count, negative_sum]


input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(input_arr))  # [10, -65]
print(count_positives_sum_negatives([]))          # []
print(count_positives_sum_negatives(None))        # []
