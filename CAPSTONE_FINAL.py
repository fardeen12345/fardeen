import random
score = 0
print("this is a mcq test; pick one answer")
answer = ''
question_ar = [["How to do while in pseudocode? ","a - WHILE ","b - while()","c - for i","d - WHILE()",'a',"A"],['What data type is ("boofoo")?','a - Boolean', 'b - Date','c - String','d - Char','c',"C"],["What sign(s) is used to indicate 'Not equal to'?","a - !=","b - /=","c - <>","d - \=","c","C"],["How do you declare an array?","a - DECLARE example : ARRAY [1:10] OF STRING", "b - DECLARE example ; ARRAY [5:4]","c - DECLARE ARRAY : example [1:10]", "d - declare example :array [1:10]","a","A"]] 

counter = 0
random.shuffle(question_ar)
print('')
name = input("What is your name: ")
while len(question_ar) != counter:
    for i in range (0,5):
        print(question_ar[counter][i])  
  
    print('') 
    print("Input your answer: ")
    answer = input()
    while answer not in ["a","b","c","d","A","B","C","D"]:
        print("The answer you typed is invalid, try again. ")
        answer = input()
  
    if answer != question_ar[counter][5] and answer != question_ar[counter][6]:
        print("Your answer is incorrect")
        print("Current score:" ,score)  
    
    else:
        score = score + 1
        print("Your answer is correct")
        print("Current score:" ,score)
    
    counter = counter + 1
    print('')

print('Score = ',score)
if score < 2:
    print("you're not the sharpest tool in the shed")
else:
    print('goodjob')

score = str(score)

file = open("highscore.txt",'a')
file.write(name)
file.write(": ")
file.write(score)
file.write('\n')
file.close()
