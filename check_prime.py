def check_prime(number):
    # if(number==2):
    #     print("Number is prime")
    #     return
    flage=True
    for i in range(2,number-1):
        if number%i==0:
            #not prime
            flage=False

    if(flage):
        print("Number is prime")
    else:
        print("Not prime")

x=int(input("Enter a numner"))
check_prime(number=x)