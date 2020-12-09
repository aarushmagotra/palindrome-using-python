total = int(input('Enter the no of numbers you want to find the palindrome of: '))
lst = []
for i in range(total):
    num = int(input('Enter a number: '))
    lst.append(num)

for value in lst:
    a = value
    while True:
        n = str(a)
        if str(n[::-1]) == str(n):
            if a == value:
                print('"{}" itself is a palindrome'.format(value))
                print()
                break
            else:
                print('The next palindromme after {} is "{}"'.format(value, a))
                print()
                break
        a += 1