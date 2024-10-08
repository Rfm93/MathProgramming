"""<p>Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with $1$ and $2$, the first $10$ terms will be:
$$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$$</p>
<p>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.</p>
"""

from time import time

t1 = time()

# Step 1: create the Fibonacci sequence

a = 0
b = 1
c = b

fibonacci = []

fibonacci.append(a)
fibonacci.append(b)

while c < 4000000:
    a = b
    b = c
    fibonacci.append(c)
    c = a + b
    

# Step 2: Find all even elements in the sequence

even_fibonacci = []

for number in fibonacci:
    if number % 2 == 0:
        even_fibonacci.append(number)
    else:
        pass

# Step 3: Sum of even numbers in the Fibonacci sequence

solution = 0

for number in even_fibonacci:
    solution += number

print(solution)

t2 = time()

elapsed = t2  - t1

print(f"Your time spent was {elapsed} seconds")
    

