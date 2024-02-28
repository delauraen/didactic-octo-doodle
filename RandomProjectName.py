import wonderwords

from wonderwords import RandomWord
    
r = RandomWord()

# TODO generate 5 project names at a time instead of 1

def main():
    while True:
        action = input("Generate another (enter) or quit (q)").strip()

        if action.lower() == "q":
            break
        firstWord = r.word(include_parts_of_speech=["adjectives"])
        secondWord = r.word(include_parts_of_speech=["nouns"])
        print(firstWord, secondWord)
    print("Goodbye!")


if __name__ == "__main__":
    main()