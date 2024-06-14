def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    make_report(file_content)

def count_words(file_content):
    words = file_content.split()
    # print(len(words))
    return words

def count_chars(file_content):
    lower = file_content.lower()
    chars = list(lower)
    dict = {}
    for char in chars:
        if char in dict:
            dict[char] += 1
        else: 
            dict[char] = 1
    # print(dict)
    return dict

def sort_on(dict):
    return dict["num"]

def make_report(file_content):
    words = count_words(file_content)
    dict = count_chars(file_content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")    

    array = []    
    for char in dict:
        if char.isalpha():
            array.append({ "char": char, "num": dict[char] })

    array.sort(reverse=True, key=sort_on)
    
    for item in array:
        print(f"The {item["char"]} character was found {item["num"]}")
main()
