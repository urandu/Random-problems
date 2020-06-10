
def question_generator(questions):
    for question in questions:
        yield question.get("short") + input(question.get("q"))


def answer_questions(questions):
    output = "|"
    for answer in question_generator(questions):
        output = output + answer + " | "
    return output


questions = [
    {
        "q": "Hi whats your name? ",
        "short": "Name :"
    },
    {
        "q": "Which year did you start writing code? ",
        "short": "Year I began coding: "
    },
    {
        "q": "Which stack is your favorite? ",
        "short": "Preferred stack: "
    },
    {
        "q": "One fact about you? ",
        "short": "Fun fact: "
    },
]

print(answer_questions(questions))


"""
The task is to write a simple function that asks one to input name, year started coding, stack and fun_fact, 
then outputs(prints) all the inputs in a single line. Screen shot code then nominate two others to do the same
"""
