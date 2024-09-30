def main():
    book_path = "books/frankenstein.txt"
    text=get_book_text(book_path)
    characters = character_count(text)
    num_words = get_num_words(text)
    filtered_list = convert_dictionary(characters)
    filtered_list.sort(reverse=True, key=sort_on)
    print(f"----Book report on {book_path}----")
    print(f"{num_words} total words in the document")
    print("")
    display_filtered_list(filtered_list)
    print("----End of Report----")
    

def display_filtered_list(list):
    for i in range(0,len(list)):
        print(f"Character {list[i]["char"]} occurred {list[i]["count"]} times")

def convert_dictionary(dict):
    char_list = []
    for char in dict:
        if char.isalpha():
            char_list.append({"char":char, "count": dict[char]})
    return(char_list)

def sort_on(dict):
    return dict["count"]

def get_num_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def character_count(text):
    character_dictionary = {}
    lowered_text = text.lower();
    for character in lowered_text:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return(character_dictionary)


main()