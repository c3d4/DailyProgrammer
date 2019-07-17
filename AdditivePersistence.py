def add_persist(n):
    add_per = 0
    while n > 9:
        n = sum_digits(n)
        add_per += 1
        print(add_per, n)
    return add_per

def sum_digits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

print('AP = {0}'.format(add_persist(int(input('Input Any Int: ')))))
