def prime_number(num):
    if num < 2:
        return "Not Prime"
    i = 2
    while i*i <= num:
        if num % i == 0:
            return "Not Prime"
        
        i += 1
    return "Prime"
print

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"