#import functions
import random
import time

#make list for answers to randomise later
answers = ['It is certain',  'It is decidedly so',  'Without a doubt',  'Yes definitely',  'You may rely on it',  'As I see it, yes',  'Most likely',  'Outlook good',  'Yes',  'Signs point to yes',  'Dont count on it',  'My reply is no',  'My sources say no',  'Outlook not so good',  'Very doubtful',  'Reply hazy try again',  'Ask again later',  'Better not tell you now',  'Cannot predict now',  'Concentrate and ask again']

#print the title
print("        ____")
print("    ,dP9CGG88@b,")
print("  ,IP  _   Y888@@b,")
print(" dIi  (_)   G8888@b")
print("dCII  (_)   G8888@@b")
print("GCCIi     ,GG8888@@@")
print("GGCCCCCCCGGG88888@@@")
print("GGGGCCCGGGG88888@@@@...")
print("Y8GGGGGG8888888@@@@P.....")
print(" Y88888888888@@@@@P......")
print(" `Y8888888@@@@@@@P'......")
print("    `@@@@@@@@@P'.......")
print("        ```........")
print("Welcome to Kevin's Magic 8 ball. Type stop at any time if you would like to quit.")
#ask the user for an input
print("Ask a yes or no question and make sure to include a question mark")
response = input(": ")

#while loop that loops forever untill the user types stop
while response != "stop":
  if "?" in response and response != "stop":
  #infinately asks for user imput and shows answer untill stop is typed or if there isnt a question mark because of the if statements
    answa = random.choice(answers)
    waitermater = random.randint(0,5)
    print("        ____")
    print("    ,dP9CGG88@b,")
    print("  ,IP  _   Y888@@b,")
    print(" dIi  (_)   G8888@b")
    print("dCII  (_)   G8888@@b")
    print("GCCIi     ,GG8888@@@")
    print("GGCCCCCCCGGG88888@@@")
    print("GGGGCCCGGGG88888@@@@...")
    print("Y8GGGGGG8888888@@@@P.....")
    print(" Y88888888888@@@@@P......")
    print(" `Y8888888@@@@@@@P'......")
    print("    `@@@@@@@@@P'.......")
    print("        ```........")
    print("The magic 8 Ball is processing your request please wait...")
    time.sleep(waitermater)
    print(answa)
    print("Ask a yes or no question and make sure to include a question mark")
    response = input(": ")
#bug in code fixed that if "and response != "stop"" isnt included code doesnt stop when stop is said
#if there is no ? included in the users input this text pops up and then asks for user input again because of while loop on line 27
  if "?" not in response and response != "stop":
    print("        ____")
    print("    ,dP9CGG88@b,")
    print("  ,IP      Y888@@b,")
    print(" dIi        G8888@b")
    print("dCII        G8888@@b")
    print("GCCIi     ,GG8888@@@")
    print("GGCCCCCCCGGG88888@@@")
    print("GGGGCCCGGGG88888@@@@...")
    print("Y8GGGGGG8888888@@@@P.....")
    print(" Y88888888888@@@@@P......")
    print(" `Y8888888@@@@@@@P'......")
    print("    `@@@@@@@@@P'.......")
    print("        ```........")
    print("You didnt include a '?' make sure to include one in your question!")
    print("Ask a yes or no question and make sure to include a question mark")
    response = input(": ")

#prints goodbye and stops code if stop is written because if stop is written the while loop stops and then line 43 through 45 initiates
print("        ____")
print("    ,dP9CGG88@b,")
print("  ,IP      Y888@@b,")
print(" dIi  . .    G8888@b")
print("dCII   ^    G8888@@b")
print("GCCIi     ,GG8888@@@")
print("GGCCCCCCCGGG88888@@@")
print("GGGGCCCGGGG88888@@@@...")
print("Y8GGGGGG8888888@@@@P.....")
print(" Y88888888888@@@@@P......")
print(" `Y8888888@@@@@@@P'......")
print("    `@@@@@@@@@P'.......")
print("        ```........")
print("Goodbye thanks for using the magic 8 ball!")
while response == "stop":
  break