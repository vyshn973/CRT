#read a number from the user and check whether it is +ve,-ve or zero
'''
Input : 10
Output : '+ve'

Input : 0
output : 'Zero'

Input : -5
Output :'-ve'

'''
n = int(input())
if n > 0:
    print("+ve")
elif n == 0:
    print("Zero")
else:
    print("-ve")