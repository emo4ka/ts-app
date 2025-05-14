# text_search_app.py

def write_to_file(text):
    with open("utf8_text.txt", "w", encoding="UTF-8") as file:
        file.write(text)

def read_file():
    with open("utf8_text.txt", "r", encoding="UTF-8") as file:
        return file.read()

def chatbot():
    sentence = read_file()
    print("First 5 characters of chatbot message:", sentence[:5])
    print("Chatbot initialized. Enter 'bye' to escape the brainrot.")

    while True:
        user_input = input("You: ").lower().strip()

        if "hi" in user_input:
            print("Bot: salam, my giga chad 🗿")
        elif "venom" in user_input:
            print("Bot: absolute cinema 💯🔥")
        elif "bye" in user_input:
            print("Bot: o7, gone but not forgotten 😔")
            break
        elif "sigma" in user_input:
            print("Bot: grindset never sleeps 🛌❌")
        elif "rizz" in user_input:
            print("Bot: unspoken, respectfully 🕴️💬💅")
        else:
            response = user_input.replace("?", "").replace("!", "")
            print(f"Bot: '{response}'? That's so based-core-corecore-core.")

def search_word_highlight():
    sentence = read_file()
    search_word = input("Enter a word to highlight: ").strip().lower()

    if search_word in sentence.lower():
        highlighted = sentence.replace(search_word, f"*{search_word}*")
        print("Highlighted sentence:", highlighted)
    else:
        print("Word not found in the text. L + ratio")

def logical_operator_search():
    sentence = read_file().lower()
    word1 = input("Enter first word: ").strip().lower()
    word2 = input("Enter second word: ").strip().lower()

    if word1 in sentence and word2 in sentence:
        print(f"Both '{word1}' and '{word2}' were found in the text! W combo")
    elif word1 in sentence or word2 in sentence:
        print(f"At least one of the words ('{word1}', '{word2}') was found. Mid tbh.")
    else:
        print("Neither word was found in the text. This ain't it chief.")

def binary_search(sorted_words, target):
    low, high = 0, len(sorted_words) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_words[mid] == target:
            return mid
        elif sorted_words[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_interface():
    sentence = read_file().lower()
    word_list = sorted(set(sentence.replace('.', '').replace(',', '').split()))
    print("Words in sorted order:", word_list)

    target = input("Enter word to search (binary search): ").strip().lower()
    index = binary_search(word_list, target)
    if index != -1:
        print(f"'{target}' found at index {index} in sorted word list. GGs.")
    else:
        print(f"'{target}' not found. skill issue.")

def goofy_alert():
    print("WARNING: You are entering the brainrot zone 🧠💥\n")

def main():
    goofy_alert()
    write_to_file("Bro was cooking 💀💀💀\nLiterally me frfr\nSigma mindset activated 🔥\nShe left me on read so I read a book 📖\nOhio final boss energy 😭")

    while True:
        print("\nChoose an option:")
        print("1 - Chatbot interaction")
        print("2 - Search and highlight a word")
        print("3 - Logical operator search")
        print("4 - Binary search in text")
        print("5 - Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            chatbot()
        elif choice == "2":
            search_word_highlight()
        elif choice == "3":
            logical_operator_search()
        elif choice == "4":
            binary_search_interface()
        elif choice == "5":
            print("Exiting program. Touch some grass 🌱")
            break
        else:
            print("Invalid choice. Try again, bozo 🤡")

if __name__ == "__main__":
    main()
