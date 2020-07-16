"""
a = int(input(" Enter 1 number : "))
b = int(input(" Enter 2 number : "))
c = int(input(" Enter 3 number : "))
l =[a,b,c]
m = max(l)
#print(m)
while (1):
    if (m % a == 0 and m % b == 0 and m % c == 0 ):
        print("The LCM is :" , m)
        break
    m = m+1
"""
"""
x = input("Enter numbers separated by space ")
l = x.split(" ")
print(l)
w = []
for i in range(len(l)):
    num = int(l[i])
    w.append(num)
print(w)
m = max(w)
print(m)
print(all(w))
print(len(w))
while True:
    z = []
    for j in range(len(w)):
        r = m % w[j]
        z.append(r)
    #print(z)
    if sum(z)==0:
        print("LCM is ", m)
        break
    else:
        m = m+1
"""

n = input("Enter numbers separated by space: ")
l = n.split(" ")
print(l)
k = []
for i in range(len(l)):
    k.append(int(l[i]))
print(k)
m = max(k)
print(m)

while True:
    r = []
    for j in range(len(k)):
        r.append(m % k[j])
    if sum(r) == 0:
        print("LCM is: {}".format(m))
        break
    else:
        m = m+1


