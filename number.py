from statistics import median, mode, multimode

numbers = [10,20,30,20,50,40,20]
summation = sum(numbers)
avg = sum(numbers)/len(numbers)
mode_num = multimode(numbers)
middle_num = median(numbers)

print(numbers)
print(summation)
print(avg)
print(mode_num)
print(middle_num)
