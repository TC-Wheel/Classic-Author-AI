# Exercise 13.8. Markov analysis:
# 1. Write a program to read a text from a file and perform Markov analysis. The result should be
# a dictionary that maps from prefixes to a collection of possible suffixes. The collection might
# be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your
# program with prefix length two, but you should write the program in a way that makes it easy
# to try other lengths.
# 2. Add a function to the previous program to generate random text based on the Markov analysis.
# Here is an example from Emma with prefix length 2:
# He was very clever, be it sweetness or be angry, ashamed or only amused, at such
# a stroke. She had never thought of Hannah till you were never meant for me?" "I
# cannot make speeches, Emma:" he soon cut it all himself.
# For this example, I left the punctuation attached to the words. The result is almost syntactically correct, but not quite.
# Semantically, it almost makes sense, but not quite.
# What happens if you increase the prefix length? Does the random text make more sense?
# 3. Once your program is working, you might want to try a mash-up: if you combine text from
# two or more books, the random text you generate will blend the vocabulary and phrases from
# the sources in interesting ways.
# Credit: This case study is based on an example from Kernighan and Pike, The Practice of Programming, Addison-Wesley, 1999.
# You should attempt this exercise before you go on; then you can download my solution from http://thinkpython2.com/code/markov.py. You will also need http://
# thinkpython2.com/code/emma.txt.
import re
import random


def read_file(s):
    with open(s, encoding="utf8") as f:
        file = f.read()
        return file


def skip_header(file):
    """
    Takes a Gutenburg(?) Project .txt file
    and removes the head and foot
    """
    pattern = re.compile(r"\s\*\*\*.+\*\*\*\s")
    matches = re.finditer(pattern, file)
    start_read = 0
    end_read = 0
    for i, match in enumerate(matches):
        if i == 0:
            s = match.span()
            start_read = s[1]
        if i == 1:
            e = match.span()
            end_read = e[0]
        # print(f"i = {i} start = {start_read} end = {end_read} match = {match.span()}")
    return file[start_read:end_read].split("\n")


def markov_analyse(file_list):
    """
    in: takes a list
    out: a markov dictionary
    """
    markov_dict = {}

    for line in file_list:
        words = line.split(" ")
        for i in range(len(words) - 1):
            word = words[i]
            if word not in markov_dict:
                markov_dict[word] = [words[i + 1]]
                continue
            value_list = markov_dict[word]
            if words[i + 1] not in value_list:
                value_list.append(words[i + 1])
    return markov_dict

    # for loop (split each element of a list into words)
    # if it's not already in the dictionary- add each word to an element titled prefix
    # if it is in the dictionary, append the word to the value list
    # return the dictionary


# def is_acceptable(markov_dict, start_word, number_of_cycles):
#     for i in range(number_of_cycles):
#         markov_dict


def print_random_text(markov_dict, number_of_cycles=20):
    # while is_acceptable(markov_dict, start_word, number_of_cycles) == False:
    #     start_word = random.choice(markov_dict)
    start_word = "He"
    previous_word = start_word
    print(start_word, end=" ")
    for i in range(number_of_cycles):
        next_word = random.choice(markov_dict.get(previous_word))
        print(next_word, end=" ")
        previous_word = next_word[:]
    # pretty good I guess. There's still some issues with knowning if a word is good or not.
    # if there's going to be some kind of error in the code, then we need to skip it
    # I could do this with 'try' and 'except' but is that a crutch?
    # also I need to figure out how to get it to stop and the end of a sentence.


def main():
    file = read_file("TheBrothers.txt")
    file_list = skip_header(file)
    markov_dict = markov_analyse(file_list)
    print_random_text(markov_dict)


if __name__ == "__main__":
    main()
