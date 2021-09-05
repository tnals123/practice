#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *
q=10
k=2
for i in range(1,6):
    for p in range(1,q):
        print(' ',end='')
    for z in range(1,k):
        print('*',end='')
    for l in range(1,k-1):
        print('*',end='')
    print('')
    q-=1
    k+=1
num1=7
num2=4
for num3 in range(1,5):
    for num4 in range(1,num1):
        print(' ',end='')
    for num5 in range(1,num2):
        print('*',end='')
    for num6 in range(1,num2+1):
        print('*',end='')
    print('')
    num1+=1
    num2-=1
    