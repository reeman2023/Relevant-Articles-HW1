def words_histogram(articles):
    word_histogram = {}
    for word in articles:
        if word not in word_histogram.keys():
            word_histogram[word] = 1
        else:
            word_histogram[word] = word_histogram[word] + 1
    for irwd in irrelevant_word:
        if irwd in word_histogram:
            del word_histogram[irwd]

    word_histogram = dict(sorted(word_histogram.items(), key=lambda item: item[1], reverse=True))
    return word_histogram


def relevant_articles(article1, article2):
    count = 0
    for key in article1:
        if key in article2:
            count = count + 1

    if count >= 3:
        print("The Two Texts Are Relevant in : ", count, " Keys")
        print(article1)

    else:
        print("sorry,no relevant article")



irrelevant_word = ['\n', '.', ',', '?', '!', 'the', 'has', 'he', 'a', 'for', 'by', 'and', 'to', 'in', 'at', 'with',
                   'that','is', 'of', 'this', 'was', 'all', 'an', 'on', '-', 'i', 'it', 'are', 'or', 'not', 'as', 'have',
                   'they']
# Import Module
import os
path = r"articles"       # insert Folder Path
os.chdir(path)
lists = []    # consists of all txt files
keys_list = []


for file in os.listdir():       # iterate through all file
    with open(file, 'r') as f:
        article = f.read().lower().split(" ")
        lists.append(article)

for article in lists:
    words_histogram(article)
    keys = list(words_histogram(article).keys())[0:7]  # convert word_histogram dic. to list
    keys_list.append(keys)

in_text = input("insert your article:")
input_text = in_text.lower().split(" ")
words_histogram(input_text)
input_article = list(words_histogram(input_text).keys())[0:7]

for k in keys_list:
    relevant_articles(k, input_article)