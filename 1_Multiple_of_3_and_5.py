"""
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
"""
from time import time

t1 = time()

sequence3 = list(range(3, 1000, 3))

sequence5  = list(range(5, 1000, 5))

sequence3_5 = set(sequence3 + sequence5)

solution = sum(sequence3_5)

print(f"The sum of multiples of 3 and 5 up to 1000 was {solution}.")

t2 = time()

elapsed = t2  - t1

print(f"Your time spent was {elapsed} seconds")
