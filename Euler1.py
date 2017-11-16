nums = [3,5]
#What numbers are being used
max = 1000
# setting 1000 to max

result = 0
#stating that result starts at 0

for i in range(0,max):
    #i will equal all numbers in the range eventually, sets loop
    if i%3 == 0 or i%5 == 0:
        #if i is divisible by three or five then that number is added to the result
        result += i
print result
#prints the equation
