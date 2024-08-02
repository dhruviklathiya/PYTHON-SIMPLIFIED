# Calculating time to run the code
import time

start = time.time()
sum = 0
for i in range(0,101):
    sum+=i
print(sum)
end = time.time()

print(f"Total time to run code: {end-start}")
