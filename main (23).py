# from datetime import date
# def calculator():
#     while True:
#         try:
#             num1=float(input("ჩაწერეთ პირველი რიცხვი:"))
#             break
#         except ValueError:
#             print("მხოლოდ რიცხვი უნდა შეიყვანოთ!")
#     while True:
#         try:
#             num2=float(input("ჩაწერეთ მეორე რიცხვი:"))
#             break
#         except ValueError:
#             print("მხოლოდ რიცხვი უნდა შეიყვანოთ!")
#     while True:
#         operation=input("აირჩიეთ მოქმედება: + ან -,ან * ან /:   ")
#         if operation in ["+", "-", "*", "/"]:
#             break
#         else:
#             print("აირჩიეთ სწორი მოქმედება")
#         if operation == "+":
#           result = num1+num2
#         elif operation == "-":
#           result = num1-num2
#         elif operation == "*":
#           result = num1*num2
#         elif operation == "/":
#             if num2 == 0:
#                 print("ნულზე გაყოფა არ შეიძლება!")
#                 return
#             result = num1 / num2
#         print(f"შედეგი: {result}")


#         finishtime = date.today()

#         with open("actions.txt", "a") as file:
#             file.write(f"{num1} {operation} {num2} = {result}  {finishtime}\n")
#         print("შედეგი შენახულია actions.txt ფაილში")

# calculator()

from datetime import date

def calculator():

    while True:
        try:
            num1 = float(input("ჩაწერეთ პირველი რიცხვი: "))
            break
        except ValueError:
            print("მხოლოდ რიცხვი უნდა შეიყვანოთ!")

    while True:
        try:
            num2 = float(input("ჩაწერეთ მეორე რიცხვი: "))
            break
        except ValueError:
            print("მხოლოდ რიცხვი უნდა შეიყვანოთ!")

    while True:
        operation = input("აირჩიეთ მოქმედება: + ან - ან * ან /: ")

        if operation in ["+", "-", "*", "/"]:
            break
        else:
            print("აირჩიეთ სწორი მოქმედება")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("ნულზე გაყოფა არ შეიძლება!")
            return
        result = num1 / num2

    print(f"შედეგი: {result}")

    finishtime = date.today()

    with open("actions.txt", "a") as file:
        file.write(f"{num1} {operation} {num2} = {result}  {finishtime}\n")

    print("შედეგი შენახულია actions.txt ფაილში")


calculator()
