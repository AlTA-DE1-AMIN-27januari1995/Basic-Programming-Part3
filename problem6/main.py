def prima(N):
    if N < 2:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

def full_prima(num):
    # Periksa apakah bilangan itu sendiri adalah prima
    if not prima(num):
        return False
    
    # Ambil setiap digit dari bilangan dan periksa apakah itu adalah bilangan prima
    for digit in str(num):
        if not prima(int(digit)):
            return False
    
    return True

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True
