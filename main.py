numbers=list(map(int,input().split()))
x=[]
y=[]
z=[]
n=[]
p=[]
print("1. Maximum number =",max(numbers))
print("2. Minimum number =",min(numbers))
print("3. Sum of the numbers = ",sum(numbers))
print("4. Average of the numbers = ",int((sum(numbers)/len(numbers))))
print("5. Second maxinum number =", sorted(numbers)[-2])
for i in numbers:
    if i%2==0:
        x.append(str(i))
    else:
        y.append(str(i))
print("6. Even numbers =" ,", ". join(x))
print("7. Odd numbers =" ,", ". join(y))
for i in numbers:
    if 9<i<100:
        z.append(str(i))
print("8. Two digit numbers =" ,", ". join(z))
for i in numbers:
    if i>0:
        p.append(str(i))
    else:
        n.append(str(i))
print("9. Negative numbers =",", ". join(n))
print("10. Positive numbrs =",", ".join(p))




