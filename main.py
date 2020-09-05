def intOrfloat(num):
    try:num = int(num)
    except:num = float(num)
    return num
def main():
    num1 = (intOrfloat(input("Enter first number: ")))
    num2 = (intOrfloat(input("enter second number: ")))

    print(num1+num2)

if __name__ == '__main__':
    main()