def divisible_numbers(start, end):
    if type(start) == int and type(end) == int:
        if start < end:
            print("Even numbers divisible by 2: "+str([i for i in range(start, end+1) if i % 2 == 0]))
            print("Odd numbers divisible by 3: " + str([i for i in range(start, end+1) if i % 3 == 0]))
            print("Numbers not divisible by 2 and 3: " + str([i for i in range(start, end + 1) if i % 3 != 0 and i % 2 != 0]))

divisible_numbers(1,10)