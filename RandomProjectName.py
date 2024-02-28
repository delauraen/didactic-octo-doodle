import wonderwords

from wonderwords import RandomWord
    
r = RandomWord()

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