def product(a, b):
    if a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    result = a * b
    print("Product of", a, "and", b, "equals", result)
    return result

def pre_product(a, b):
    if a > 0 and b > 0:
        product_result = product(a,b)
    else:
        product_result = -1 * product(a, b)
        print("ha-ha, just kidding, actually",
              "product of", a, "and", b, "equals", product_result)
    return product_result

a, b = [int(x) for x in input().split()]
pre_product(a, b)
