questions = [
    {
        "question": "What is the capital of Belgium?",
        "options": ["A. Ghent", "B. Antwerp", "C. Brussels", "D. Liège"],
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for web styling?",
        "options": ["A. Python", "B. CSS", "C. Java", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "How many days are in a leap year?",
        "options": ["A. 365", "B. 360", "C. 364", "D. 366"],
        "answer": "D"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyper Text Markup Language", "B. High Tech Modern Language", "C. Hyper Transfer Markup Logic", "D. Home Tool Markup Language"],
        "answer": "A"
    },
    {
        "question": "Which planet is closest to the sun?",
        "options": ["A. Venus", "B. Earth", "C. Mercury", "D. Mars"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print(q["question"])

    for a in q["options"]:
        print(a)
    
    answer = input("Answer: ").upper()

    if answer == q["answer"]:
        score += 1
    
print(f"You scored {score} out of {len(questions)}!")
