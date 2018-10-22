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

word_love_count = word_count('love'.lower())
her_message = word_count('niru:'.lower())
his_message = word_count('Akshay Deshpande:'.lower())
media_shared = word_count('Media omitted'.lower())

print(f"The word love has been used {word_love_count} number of times")
print(f"Akshay has messaged {his_message} number of times")
print(f"Niru has messaged {her_message} number of times")
print(f"Images/Audio files have been share {media_shared} number of times")



