#! /usr/bin/python3

import sys #sys provides access to cli arguments, in particular .argv provides list of strings
#python3 main.py ==> [main.py] ==> 1 list
#While python3 main.py path\to\book ==> [main.py], [path] ==> 2 list

from stats import word_count
from stats import char_counts
from stats import pretty_dict_list

def get_book_text(file_path): #reading file

    try: #if file not exist, Exit gracefully
        with open(file_path) as f:
            file_content = f.read() #saving as string
    except Exception as e:
        print(e)
        sys.exit(2)

    word_count(file_content) #counting words
    return file_content
    
def main():
    if len(sys.argv) != 2: #if no 2 argv exit with err 1
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    file_content = get_book_text(book_path)
    #print(file_content)

    print("--------- Character Count -------")
    num_char = char_counts(file_content) #count char and save as dict as char:count

    pretty_list = pretty_dict_list(num_char) #list of {char:num} ==> {char:value, num:value}

    
    #print(pretty_list)
    for i in pretty_list: #formatting 
        char = i["char"]
        if char.isalpha(): #check wether char is alphabet or symbols
            print(f"{char}: {i["num"]}")

    print("============ END ============")

main()