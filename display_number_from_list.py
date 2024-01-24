#define a function for list
def divisible_by_five(list):
#for loop through the list using list comprehension and return numbers that divisible by five
    return [numbers for numbers in list if numbers % 5 == 0]
#list of numbers
numbers = [10, 20, 33, 46, 55]
#print the given list:
print("Given list:", numbers)
#getting numbers divisible by 5
#print divisible by 5:
#print numbers divisible by 5
