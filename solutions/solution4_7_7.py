def prime_numbers(lmt):
    primes = [2]
    for i in range(3, lmt+1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
            if p > i/2:
                break
        if is_prime:
            primes.append(i)
    return primes


if __name__ == "__main__":
    lmt = int(input())
    print(prime_numbers(lmt))
