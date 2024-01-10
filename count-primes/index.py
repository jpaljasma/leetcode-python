import math

"""
Amazon math question - Count Primes (Medium)
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Given an integer n, return the number of prime numbers that are strictly less than n.
        """
        if n < 2:
            return 0
        
        # create array of 1-n that marks all elements true
        is_prime = [True] * n
        # Prime numbers start from 2
        is_prime[0] = is_prime[1] = False

        for i in range (2, math.ceil(math.sqrt(n))):
            if is_prime[i] == True:
                for multiple_of_i in range(i * i, n, i):
                    is_prime[multiple_of_i] = False

        return sum(is_prime)

    def countPrimesBruteForce(self, n: int) -> int:
        """
        Brute force example that will run VERY slow as the number grows
        Given an integer n, return the number of prime numbers that are strictly less than n.
        """
        num_primes = 0
        is_prime = False

        for i in range (2, n):
            is_prime = True
            for j in range(2, i):
                if 0 == i%j:
                    is_prime = False
                    break
            if is_prime == True:
                num_primes += 1

        return num_primes

    

print(Solution().countPrimes(47))