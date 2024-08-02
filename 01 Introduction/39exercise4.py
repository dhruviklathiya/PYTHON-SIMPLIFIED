# Finding prime numbers from user input
n = int(input("Till how many numbers do you want to check number is prime or not?"))
prime_dict = {}
for i in range(0,n+1):
    if i<=1:
        prime_dict[i] = True
    else:
        for j in range(2,round(i**0.5)+1):
            if i%j==0:
                prime_dict[i]=False
                break
            prime_dict[i] = True

for i,j in prime_dict.items():
    print(f"{i}=======>{j}")

# Why we have use square root?
    # When determining if a number n is prime, you only need to check divisors up to the square root of n because of the properties of factor pairs.
# Why not cube root?
    # Because using the cube root doesn't align with the fundamental factorization logic for primes. The square root works because it directly ties to the smallest possible factors of n.
