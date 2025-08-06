def word_count(content): #counting words
    words = content.split()
    num_words = len(words)

    print(f"Found {num_words} total words")



def char_counts(text): #counting char and saving it into dict as char:num
    letters = {}
    for i in text:
        j = i.lower()
        if j not in letters:
            letters[j] = 1
        else:
            letters[j] += 1

    return letters

def pretty_dict_list(og_dict): #list of {char:num} ==> {char:value, num:value}... 
    pretty_list = []
    for i in og_dict:
        #{"char": "b", "num": 4868}
        pretty_dict = {"char": i, "num": og_dict[i]}
        pretty_list.append(pretty_dict)
        pretty_list.sort(reverse=True, key=sort_on) #sort by num and desending order
    return pretty_list

def sort_on(og_list): #on which to sort the list
    return og_list["num"]
