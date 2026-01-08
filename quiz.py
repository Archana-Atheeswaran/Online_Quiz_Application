def start_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
            "answer": "Delhi"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["Python", "HTML", "C", "Java"],
            "answer": "HTML"
        },
        {
            "question": "What does CSS stand for?",
            "options": [
                "Cascading Style Sheets",
                "Computer Style Sheet",
                "Creative Style System",
                "Colorful Style Sheet"
            ],
            "answer": "Cascading Style Sheets"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        user_choice = int(input("Choose option (1-4): "))
        if q["options"][user_choice - 1] == q["answer"]:
            score += 1

    print(f"\nYour Score: {score}/{len(questions)}")


start_quiz()
