import random
print("===================================")
print("      📚 Welcome to Quiz App      ")
print("===================================")

#Questions
question = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Multan"],
        "answer": "Islamabad"
    },
    {
        "question": "Who developed Python?",
        "options": ["Elon Musk", "Guido van Rossum", "Mark Zuckerberg", "Bill Gates"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which one is a Python data type?",
        "options": ["Banana", "Integer", "Slide", "Bottle"],
        "answer": "Integer"
    },
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Multan"],
        "answer": "Islamabad"
    },
    {
        "question": "Who developed Python?",
        "options": ["Elon Musk", "Guido van Rossum", "Mark Zuckerberg", "Bill Gates"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which one is a Python data type?",
        "options": ["Banana", "Integer", "Slide", "Bottle"],
        "answer": "Integer"
    },
    {
        "question": "Which company developed Windows OS?",
        "options": ["Apple", "Google", "Microsoft", "IBM"],
        "answer": "Microsoft"
    },
    {
        "question": "HTML stands for?",
        "options": ["HyperText Markup Language", "Home Tool Markup Language", "HyperTool Multi Language", "HighText Machine Language"],
        "answer": "HyperText Markup Language"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "func"],
        "answer": "def"
    },
    {
        "question": "Which of these is a valid Python loop?",
        "options": ["repeat", "while", "iterate", "do"],
        "answer": "while"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Control Panel Unit", "Computer Power Unit", "Central Power Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["//", "<!-- -->", "#", "/* */"],
        "answer": "#"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["echo()", "print()", "printf()", "cout<<"],
        "answer": "print()"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "options": ["Steve Jobs", "Jeff Bezos", "Elon Musk", "Bill Gates"],
        "answer": "Bill Gates"
    },
    {
        "question": "Which data structure works on FIFO?",
        "options": ["Stack", "List", "Queue", "Set"],
        "answer": "Queue"
    },
    {
        "question": "Which tag is used for heading in HTML?",
        "options": ["<p>", "<h1>", "<head>", "<title>"],
        "answer": "<h1>"
    },
    {
        "question": "What is the extension of Python file?",
        "options": [".py", ".java", ".txt", ".exe"],
        "answer": ".py"
    },
    {
        "question": "Which one is used to take input from user in Python?",
        "options": ["scan()", "input()", "cin>>", "get()"],
        "answer": "input()"
    },
    {
        "question": "Which year was Pakistan created?",
        "options": ["1947", "1952", "1965", "1940"],
        "answer": "1947"
    },
    {
        "question": "Who is the national poet of Pakistan?",
        "options": ["Allama Iqbal", "Faiz Ahmed Faiz", "Ahmed Faraz", "Mirza Ghalib"],
        "answer": "Allama Iqbal"
    },
    {
        "question": "Which keyword is used for condition checking in Python?",
        "options": ["if", "when", "check", "cond"],
        "answer": "if"
    },
    {
        "question": "Which city is called the City of Lights in Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Karachi"
    },
    {
        "question": "Which built-in Python function gives the length of a list?",
        "options": ["size()", "count()", "length()", "len()"],
        "answer": "len()"
    }
]
score = 0
random.shuffle(question)
for i,q in enumerate(question):
    print(f"\nQ{i+1}:{q['question']}")

    options = q["options"]
    random.shuffle(options)

    for idx,option in enumerate(options):   
        print(f"{chr(65+idx)}.{option}")

    answer = input("Your Answer is (A/B/C/D): ").strip().upper()

    if answer in ["A","B", "C", "D"]:
        selected = options[ord(answer) - 65]
    
        if selected == q["answer"]:
            print("Correct Answer")
            score+=1
        else:
            print(f"Wrong Answer: {q['answer']}")
    else:
        print("Invalid Input")

print("\n =========== Quiz Finised ===========")
print(f"You Got {score} out of {len(question)}")
percentage = (score / len(question)) * 100
print(f"Percentage : {percentage:.2f}%")  

if percentage == 100:
    print("Execelent Job")
elif percentage >= 60:
    print("Good Job")
else:
    print("Keep Practice")