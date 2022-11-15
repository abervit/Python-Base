# Exponent function

def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result


print(raise_to_power(6, 5))  # --> 7776


def raise_to_power1(base_num, pow_num):
    return base_num ** pow_num


print(raise_to_power1(6, 5))  # --> 7776
