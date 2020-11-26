#import WordCloud

#initialize variables

words = ""
newwords = ""
frequencies = {}
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#Create unintersting words list
unwords = ["a", "the", "to", "if", "in"]

#import text file and normalize to lower case
file = open(r"C:\Project\Declaration.txt", "r")
words = file.read().lower()
file.close

#remove punctuation

for letter in words:
    if letter not in punctuations:
    #if letter.isalpha() or letter.isspace():
        newwords += letter
        

#format input for wordcloud

wordlist = newwords.split()
for word in wordlist:
    if word in unwords:
        continue
    elif word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1

print (frequencies)
    


#cloud = wordcloud.WordCloud()
#cloud.generate_from_frequencies(frequencies)
#cloud.to_file("myfile.jpg")
