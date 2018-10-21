wordLoveCount = 0
herMessage = 0
hisMessage = 0
mediaShared = 0
with open(r'C:\Users\Adeshpande\Downloads\documents\temp\WhatsAppChatwithNiru.txt', mode='r', encoding="utf8") as f:
    for line in f:
        line=line.lower()
        wordList=line.split()
        # look for the word love
        if ('love' in line):
            wordLoveCount=wordLoveCount+1

        # looks for the name of the person who has texted
        try:
            if (wordList[3] == 'akshay'):
                hisMessage = hisMessage + 1

            if (wordList[3] == 'niru:'):
                herMessage = herMessage + 1

        except IndexError:
            pass

        # looks for the media files passed
        if ('<media omitted>' in line):
            mediaShared = mediaShared+1


print(f"The word love has been used {wordLoveCount} number of times")
print(f"Akshay has messages {hisMessage} number of times")
print(f"Niru has messages {herMessage} number of times")
print(f"Images/Audio files have been share {mediaShared} number of times")



