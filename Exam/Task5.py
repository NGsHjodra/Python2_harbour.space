#Print all even integers between 5 and 15.
print([i for i in range(5,15) if i%2==0])

# or

for i in range(5,15):
    if i%2==0:
        print(i)