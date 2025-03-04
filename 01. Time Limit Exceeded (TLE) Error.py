'''
Time Limit Exceeded (TLE) Error happens when your code takes too long to run. Every programming problem has a time limit, and if your solution is too slow, it gets a TLE.

'''
#Example:
# Inefficient solution (causes TLE)
n = int(input())  
for i in range(n**2):  # Too many operations!
    print(i)

# If n = 10⁶, this loop runs 10¹² times, which is too slow.

#Solution:Optimize your code!
# Efficient solution

n = int(input())  
for i in range(n):  # Runs only 'n' times
    print(i)
