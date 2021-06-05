'''
This program takes an input text from the user and finds out the difficulty level of the given text.
It judges the readability of the given text.
This grading system is upto level 16+.
'''

text = input("Enter Text: ") #get input from user
l = len(text)
letters = 0
words = 0
sentences = 0
for i in range(l):
    #calculate number of letters
    if(text[i] >= 'a' and text[i] <= 'z'): 
        letters += 1
    elif(text[i] >= 'A' and text[i] <= 'Z'):
        letters += 1
    #calculate number of words
    elif(text[i] == ' '):
        words += 1
    #calculate number of sentences
    elif(text[i] == '.' or text[i] == '?' or text[i] == '!'):
        sentences += 1

#calculate number of letters and sentences per 100 words
words += 1
L = (letters/words)*100
S = (sentences/words)*100

#calculate final grade
grade = 0.0588*L - 0.296*S - 15.8

#printing final grade
if(grade >= 1 and grade < 16):
    G1 = round(grade)
    print("grade:", G1)
elif(grade > 16):
    print("grade: 16+")
elif(grade <1):
    print("grade < 1")