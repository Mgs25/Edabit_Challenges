def main():
    class User:
        def user_count (username,out):
            for letter in username:
                out.append(bin(ord(letter)))
            return "binary code of ascii values: " + "".join(out)
    print(User.user_count("o",[]))

if __name__ == '__main__':
    main()
