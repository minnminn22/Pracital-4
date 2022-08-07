numbers = []
i = 0
nums = 5
while i < nums:
    n = int(input('please enter number :'))
    numbers.append(int(n))
    i += 1
print('The first number is', numbers[0])
print('The last number is', numbers[4])
print('The smallest number is', min(numbers))
print('The largest number is', max(numbers))
print('The average of the numbers is', sum(numbers) / len(numbers))