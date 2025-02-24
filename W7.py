low = int(input("Enter the lower number: ")) 
high = int(input("Enter the higher number: ")) 
#even numbers divide by twos 
evens = [str(num) for num in range(low, high + 1) if num % 2 == 0] 
print(f"The even numbers between {low} and {high} are: {' '.join(evens)}") 

pnum = int(input("Enter a positive integer: ")) 
#numbers that can divide with remainder 0 are factors 
factors = [str(i) for i in range(1, pnum + 1) if pnum % i == 0] 
print(f"The integers that are factors of {pnum} are: {' '.join(factors)}") 

#set up an index of alphabet letters 
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
name = input("Enter a name: ").lower() 
total = sum(alpha.index(char) for char in name if char in alpha) 
print(f"The sum of positions in '{name}' is: {total}")  

recur = int(input("Enter a recursion integer: ")) 
def recursive(recur):
   if recur >= 1: 
     recursive(recur - 1) 
     print(recur * recur)
recursive(recur)

numbers = input("Enter a list of unsorted integers, each separated by a space: ")
nums = [int(x) for x in numbers.split()]

def teepee_sort(nums):
    # Find the maximum number
    max_num = max(nums)
    # Create odd and even lists excluding the max number
    odds = sorted([x for x in nums if x % 2 != 0 and x != max_num])
    evens = sorted([x for x in nums if x % 2 == 0 and x != max_num], reverse=True)
    # Combine lists with max in center
    return odds + [max_num] + evens

result = teepee_sort(nums)
print(f"TeePee sorted: {' '.join(str(x) for x in result)}")