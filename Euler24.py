import itertools # finds and defines the module we are going to use
x = itertools.permutations('0123456789', 10)
counter = 0
for i in x:
    counter += 1
    if counter == 1000000: #we only need to go to 1000000 so that is our max number
        print i #prints the results from i
    else: #selects exactly one of the suites by evaluating the expressions one by one until one is found to be true
        pass #used when we need the code to complete but dont want to command or excute
