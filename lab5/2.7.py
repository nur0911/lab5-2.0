def get_prime_numbers(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for divisor in primes:
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes