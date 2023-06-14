from art import logo
print(logo)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
flage = True
while flage:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
    text = input("type you message\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    def casar(start_text,shift_amount,cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text+=char
        print(f"The {cipher_direction}d text is {end_text}\n")




    casar(start_text=text,shift_amount=shift,cipher_direction=direction)
    x=input("enter yes to run again ? OR enter no to exit ? \n").lower()
    if x == "no":
        flage = False
        print("GOOD BYYE")

