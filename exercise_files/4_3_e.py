

primes = [2]

for n in range(3, 10000):
  for factor in primes:
    if factor > n ** 0.5:
      primes.append(n)
      break
    if n % factor == 0:
      break
    

print(primes)