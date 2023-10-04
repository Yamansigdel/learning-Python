def translate(word):
    result=""
    for letter in word:
        if letter in "AEIOUaeiou":
            result=result+"g"
        else:
            result=result+letter
    return result

print(translate(input("Enter your word: ")))
