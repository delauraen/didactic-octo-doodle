import wonderwords

from wonderwords import RandomWord
    
r = RandomWord()

def main():
    while True:

        for i in range(5):
            firstWord = r.word(include_parts_of_speech=["adjectives"])
            secondWord = r.word(include_parts_of_speech=["nouns"])
            print(firstWord, secondWord)

        action = input("Generate another (enter) or quit (q)").strip()

        if action.lower() == "q":
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()