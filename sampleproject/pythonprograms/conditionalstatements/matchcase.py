char = "E"
match char:
    case "A" | "E" | "I" | "O" | "U":
        print(char, "It is a Vowel")
    case _:
              print("It is a Consonant")

