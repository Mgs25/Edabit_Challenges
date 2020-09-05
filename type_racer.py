def main():
    text = "This is Methran"
    print("Text to be entered: "+text)
    i = 1
    while i == 1:
        if input("Enter Text Message: ") != text:
            return "you mistyped"

if __name__ == '__main__':
    main()
