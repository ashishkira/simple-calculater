
def main():
    while go == "go":
        number1 = int(input("Enter your fist number : "))
        oparator = input("Enter you oparator : ")
        number2 = int(input("Enter your second name : "))
        
        if oparator == "+":
            result = number1 + number2
            print(result)
        elif oparator == "-":
            result = number1 - number2
            print(result)
        elif oparator == "*":
            result = number1 * number2
            print(result)
        elif oparator == "/":
            result = number1 / number2
            print(result)
        else:
            print("bye..")
            break
#just comment
go = "go"

main()