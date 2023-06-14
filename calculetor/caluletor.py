def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
opretion = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    from calculetor_art import logo
    print(logo)
    flage =True
    num1=float(input("Enter frist number"))
    for key in opretion:
        print(key)
    while flage:
        opretion_key=input("pick up the opretion :")
        num2=float(input("Enter next number"))
        calculetor_funtion=opretion[opretion_key]
        answer = calculetor_funtion(num1,num2)
        print(f"{num1} {opretion_key} {num2}={answer}")
        var = input("Enter Y for Coutinue calculetion OR N for Start new caluletor OR E for exit").lower()
        if var=="y":
            num1=answer
        elif var=="n":
            flage=False
            calculator()
        elif var=="e":
            return print("Thank for using")




calculator()













