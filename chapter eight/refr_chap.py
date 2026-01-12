
# example of refractoring
def weighted_mean(num_list, weights_list):
    if not (num_list or weights_list):
        return None
    total = 0
    for i in range(len(num_list)):
        total += (num_list[i] * weights_list[i])
    return (total / sum(weights_list))

# test in test.py