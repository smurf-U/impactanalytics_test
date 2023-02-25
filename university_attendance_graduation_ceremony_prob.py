"""
## Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29

for 10 days: 372/773
"""



def count_attendance(n, m):
    combination = [1] * (m + 1)
    combination[m] = 0
    for ind in range(1, n+1):
        prob = [0] * (m+1)
        for jind in range(m - 1, -1, -1):
            prob[jind] = combination[0] + combination[jind+1]
        prob, combination = combination, prob
    
    return f"{prob[1]}/{combination[0]}"

  
if __name__ == "__main__":
    n = int(input("Nth day: "))
    m = int(input("Leave threshold: "))
    print(count_attendance(n, m))
