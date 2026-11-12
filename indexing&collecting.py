def main():
    code = input("give me the secret code: ")
    codeLength = len(code)

    if codeLength == 1:
        code = int(code)
    else:
        code = str(code)

    print(f"{type(code)}")
    print(f"{codeLength}")

    if type(code) == str:
        print(f"first: {code[0]}")
        print(f"last: {code[-1]}")
        if codeLength > 2:
            if codeLength % 2 == 1:
                print(f"middle: {code[codeLength // 2]}")
            
            else:
                print(f"middle 2: {code[codeLength // 2 -1]} and {code[codeLength // 2]}")
if __name__ == "__main__":
    main()
