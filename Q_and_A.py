

print( "                      ",           "WELCOME TO PYTHON quiz!")
print("Brief python:","Python is a general-purpose, interpreted, high-level programming language popularly used for website development, data analytics and automation.")
print( "                      ",           "Lets start the python Quiz!")

questions=[
    {"question": "what is the correct spelling?","options":["pythin","python","pythoni"],"answer": "python"},
    {"question": "what is the correct syntax to output 'HELLO WORLD' in python?","options":["console(hello world)","print(hello word)","print('hello world')"],
    "answer":"print('hello world')"},
    {"question": "How many datatypes in python?", "options":[5,6,10,],"answer": 5},
    {"question": "how do you create variable with the int?","options":["a=int","b=float","a=none"],"answer":"a=int"},
    {"question": "which method using the value resuable called?", "options":["datatypes","function","operators"],"answer":"function"},
    {"question": "what is list methods?", "options":["immutable","key pairs","mutable"],"answer":"mmutable"},
    {"question": "what is concept of oops?","options":["Polymorphism","Encapsulation","Inheritance","All the above","Abstraction"],"answer":"All the above"},
    {"question": "which operator methods  using the binary value called?","options":["logical operators","bitewise operators","assigment operators"],"answer":
      "bitewise operators"},
    {"question":  "which operators using this floor symbol?", "options":["**","//","<="], "answer":"//"},
    {"question": "which one is correct syntax?", "options":["a//b","a/*","a\*"],"answer":"a//b"},
    {"question": "who invented the python?","options":["guido van rossum"," James Gosling"," James Gosling"],"answer":"guido van rossum"},
    {"question": "GUL means?","options":["global intrepeted lock","graphics interface user"],"answer":"graphics interface user"},
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    answer = input("Your answer (1/2/3/4/5): ")
    if q["options"][int(answer) - 1] == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print(f"\nYour final score: {score}/{len(questions)}")
print("                    ",      "THANK YOU!")
