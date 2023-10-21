def prime_finder(n):
    # Write your code here
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    are_prime = []
    for prime in primes:
        if prime > n:
            break
        elif (prime / prime == 1) and (prime / 1 == prime):
            are_prime.append(prime)
    return are_prime

print(prime_finder(11))