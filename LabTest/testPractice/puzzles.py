def get_word_list(file_name):
    """ Read the word_list.txt file and returns a list with one word per element.
        Each word in the list is in lower case.
        For example: [aarhus, aaron, ababa, aback, ...]. """

    try:
        data_file = open(file_name, "r")
    except IOError:
        print("File could not be opened.")
        exit()

    word_list = []  # start with an empty word list
    for word in data_file:  # for every word (line) in the file
        # strip off end−of−line characters and make each word lowercase
        # then append the word to the word list
        word_list.append(word.strip().lower())
    return word_list

def puzzle_a(words):
    """ Find 5 uncapitalized, unhyphenated words that contain 9
        of the letters of the alphabet from l to v ("lmnopqrstuv"). """
    
    target_letters = "lmnopqrstuv"
    result = []

    for word in words:
        if word.islower() and '-' not in word:
            letter_count = 0
            letters_found = ""

            for char in word:
                if char in target_letters and char not in letters_found:
                    letter_count += 1
                    letters_found += char
            
            if letter_count == 9:
                result.append(word)

    for word in result[:5]:
        print(word)


def puzzle_b(words):
    """ What words consist of two consecutive pronouns? """
    pronouns = ['thou', 'thee', 'thine', 'thy', 'i', 'me', 'mine', 'my',
                'we', 'us', 'ours', 'our', 'you', 'yours', 'your', 'he', 'him',
                'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them',
                'theirs', 'their']
    
    
    for p1 in pronouns:
        for p2 in pronouns:
            for word in words:
                if p1 + p2 == word:
                    print(word)
                    break



def puzzle_c(words):
    """ Find all uncapitalized, seven-letter words, containing just
        a single vowel that does not have the letter s anywhere within it. """
        

    for word in words:
        
        if word != word.lower():
            continue

        if len(word) != 7:
            continue

        count = 0

        for char in word:
            if char in "aeiou":
                count += 1

        if count != 1:
            continue

        if "s" in word:
            continue

        print(word)


def puzzle_d(words):
    """ When you are writing in script, there are four letters of the
        alphabet that cannot be completed in one stroke: i and j (which require dots)
        and t and x (which require crosses). Find a word that uses each of
        these letters exactly once. """
    target_letters = "ijtx"

    for word in words:
        all_present = True

        for letter in target_letters:
            if word.count(letter) != 1:
                all_present = False
                break

        if all_present:
            print(word)


# Main code
word_list = get_word_list("word_list.txt")
print("*Puzzle a*")
puzzle_a(word_list)

print("\n*Puzzle b*")
puzzle_b(word_list)

print("\n*Puzzle c*")
puzzle_c(word_list)

print("\n*Puzzle d*")
puzzle_d(word_list)
