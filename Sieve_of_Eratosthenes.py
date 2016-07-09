def primes_sieve(n):
    not_prime = [False] * n
    primes = []

    for i in range(2, n):
        if not_prime[i]:
            continue
        for f in xrange(i*i, n, i):
            not_prime[f] = True

        primes.append(i)

    return primes


def data():
    n = 100
    print primes_sieve(n+1)


if __name__ == '__main__':
    data()
