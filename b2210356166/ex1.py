N=int(input("enter a number"))
sodd=0
seven=0
count=0
for i in range(1, N+1):
    if i%2 !=0:
        sodd += i
    else:
        seven += i
        count += 1
avg= seven/count
print("sum of odd numbers=", sodd)
print("average of even numbers=", avg)
