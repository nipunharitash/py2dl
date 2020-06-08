tree = input("How Big a Tree Do You Want to Plant (Enter BIG , MEDIUM , SMALL : ")
if(tree.lower() == 'big'):
    i = 41
elif(tree.lower() == 'medium'):
    i = 25
elif(tree.lower() == 'small'):
    i=15
else:
    print("Enter a Valid SIZE")
    i = 0
stem_width = i
j = 0
while(i >=0 and j <= i):
    print(' ' * i , 2*('*' * j) , ' '* i)
    i = i - 1
    j = j + 1
n = stem_width
m = int((2 * n) + 2 )
q = int(m/5)
stem_length = int(j/3)

for stem in range(stem_length):
    print(' ' * (2 *q), ('|' * q), ' ' * (2 *q))
print(" ")
print("Thank You Planting a" , "--" , tree.upper() , "TREE --")

