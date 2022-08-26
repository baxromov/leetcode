def findRestaurant(list1, list2):
    res = list()
    list1_size, list2_size = len(list1), len(list2)
    for min_sum in range(list1_size + list2_size - 1):
        for i in range(min_sum + 1):
            if i < list1_size and min_sum - i < list2_size and list1[i] == list2[min_sum - i]:
                res.append(list1[i])
        if len(res) > 0:
            break
    return res