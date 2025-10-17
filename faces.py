def main():
    userInput = input("User Input: ")
    print(convert(userInput))

def convert(str):
    result = str.replace(":)", "🙂")
    result = result.replace(":(", "☹️")
    return result

if __name__ == "__main__":
    main()