from collections import Counter

word_love_count = 0
her_message = 0
his_message = 0
media_shared = 0

def word_count(word):
    word_counting_element=0
    with open(r'C:\Users\Adeshpande\Downloads\documents\temp\WhatsAppChatwithNiru.txt', mode='r', encoding='utf8') as f:
        for line in f:
            line=line.lower()
            if (word in line):
                word_counting_element=word_counting_element+1

    return word_counting_element

def unique_words():
    all_words = Counter()
    only_string = Counter()
    words_to_ignore = ['akshay', 'niru:', 'deshpande:', '<media', 'omitted>', '-']
    with open(r'C:\Users\Adeshpande\Downloads\documents\temp\WhatsAppChatwithNiru.txt', mode='r', encoding='utf8') as f:
        for line in f:
            line=line.lower()
            all_words.update(line.split()) #this update works only when line is a list. https://stackoverflow.com/questions/40138124/elegant-way-of-adding-a-set-to-a-counter-in-python

    #below loop removes the default text added to chat from whatsapp
    for word in list(words_to_ignore):
        if word in all_words:
            del all_words[word]

    #to get only the counter containing strings
    for elements in list(all_words):
        if elements.isalpha():
            pass

    #print(f'Top 10 words are {all_words.most_common(1000)}')
    print(f'There were a total of {len(only_string)} unique words/symbols used in the chat')
    print(f'These are only strings {only_string}')

unique_words()

word_love_count = word_count('love'.lower())
her_message = word_count('niru:'.lower())
his_message = word_count('Akshay Deshpande:'.lower())
media_shared = word_count('Media omitted'.lower())

print(f"The word love has been used {word_love_count} number of times")
print(f"Akshay has messaged {his_message} number of times")
print(f"Niru has messaged {her_message} number of times")
print(f"Images/Audio files have been share {media_shared} number of times")



