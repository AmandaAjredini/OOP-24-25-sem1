import string


def add_word(word, word_count_dict):
   """Update the word frequency: word is the key, frequency is the value"""
   if word in word_count_dict:
       word_count_dict[word] += 1
   else:
       word_count_dict[word] = 1

def process_line(line, word_count_dict):
   """Process the line to get lowercase words to add to the dictionary"""
   line = line.strip()
   word_list = line.split()
   for word in word_list:
       word = word.lower().strip()
       # get comas, periods, and other punctuation as well
       word = word.strip(string.punctuation)
       add_word(word, word_count_dict)


# Create dictionary of frequencies
word_count_dict = {}
file = open("hare_and_tortoise.txt", "r")
for line in file:
   process_line(line, word_count_dict)
print(word_count_dict)

# Create list of stopwords
file = open("stopwords.txt", "r")
stopwords = []
for word in file:
    stopwords.append(word.strip())

# Create html file
html = """<!DOCTYPE html><html><head lang="en"><meta charset="UTF-8"><title>Tag Cloud Generator</title></head><body><div style="text-align: center; width: 10%; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">"""

for word, count in word_count_dict.items():
    if word not in stopwords:
        html += f'<span style="font-size: {count*2}px"> {word} </span>'

html += "</div></body></html>"

fo = open("output.html", "w")
fo.write(html)
fo.close()






