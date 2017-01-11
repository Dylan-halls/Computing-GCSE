nums = list(input(">>> "))
output = []

def sort(nums):
   print("OLD:", list(nums))
   while nums:
   	  s = min(nums)
   	  i = nums.index(s)
   	  output.append(nums.pop(i))

sort(nums)
print("NEW:", output)