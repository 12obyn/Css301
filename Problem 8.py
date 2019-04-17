#Deshawn Smith # Again
#4/9/2019

#This will tell you how many words are a length of 4 letters

wordlist = ["word", "good", "mood", "food", "robin", "shop", "computer", "crown", "anubis"]

count = 0

for word in wordlist:
    if (len(word)) == 4:
        count += 1
print(count)
