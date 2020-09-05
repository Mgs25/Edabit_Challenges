def fuzz_buzz(num):

    for i in range(0,num):
        print(i)
        print("fizz"*(i%3==0) + "buzz"*(i%5==0))


print(fuzz_buzz(20))
