#Summation-2. Print the sum of all integers between 5 and 15 inclusive, which are divisible by 3.
print(sum(i for i in range(5,15) if i%3==0))

# or
sm = 0
for i in range(5,15):
    if i%3==0:
        sm+=i

print(sm)