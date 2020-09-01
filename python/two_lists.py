
def merge(left, right):
    idx_left, idx_right = 0, 0
    result = []
    while (idx_left < len(left)) & (idx_right < len(right)):
        if left[idx_left] <= right[idx_right]:
            result.append(left[idx_left])
            idx_left += 1
        else:
            result.append(right[idx_right])
            idx_right += 1
    result.extend(left[idx_left:])
    result.extend(right[idx_right:])
    return result


print(merge([1, 2, 3, 4], [5, 6, 7, 19, 110]))
