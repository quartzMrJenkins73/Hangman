'''Hangman game'''

#Step one is to open the file that contains a list of over 200000 words.

import random

# word_list=open("sowpods.txt", "r")
def create_wordlist():
    dictionary = {}
    with open("sowpods3.txt", "r") as wordlist:
        for line in wordlist:
            (key, value) = line.split()

            dictionary[int(key)] = value
    return dictionary

def get_random_word():
    random_index = random.randint(0, len(word_list))
    random_word = word_list[random_index]
    print (f"The random word is {random_word}")
    return word_list[random_index]

word_list = create_wordlist()
print(word_list)
print(len(word_list))
random_word=get_random_word()
print(random_word)
print(get_random_word())
        # print('\ntext file to dictionary=\n', dictionary)
# lines = open('sowpods.txt').read().splitlines()  # creates a list with one line per iteù
# randomLine = random.choice(lines)
# print(lines)

    # lines = open('file.txt').read().splitlines()  # creates a list with one line per item
    # randomLine = random.choice(lines)  # pick up a random item in this list
    # for index, line in enumerate(wordlist):
    #     print("{} {}".format(index, line.strip()))
    #     with open("sowpods3.txt", "a") as sowpods:
    #         sowpods.write("{} {}".format(index, line.strip()))
    #         sowpods.write("\n")

    # lines = wordlist.readlines()

    # for index, line in enumerate(lines):
    #     print("Line {}: {}".format(index, line.strip()))


    # line = wordlist.readline()
    # cnt=1
    # while line:
    #     print("line {}: {}".format(cnt, line.strip()))
    #     line = wordlist.readline()
    #     cnt += 1
    # word=wordlist.readlines(4)
    # print (word)

