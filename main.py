from manage_problems import get_sorted_problems, divide_problem_buckets
from model import generate_question
# Formatting the problems
non_bucketed_problems = get_sorted_problems('problems.json')
example_problems = divide_problem_buckets(non_bucketed_problems)
# Generating the mock test
mock_test = []
for i in range(1, 3):
    mock_test.append(generate_question(i, example_problems))
print(mock_test)

with open('mocks/mock_test.txt', 'w') as mock:
    mock.write("\\section{Problems}\n")
    for problem in mock_test:
        mock.write(f"\\subsection{{Problem {problem['number']}:}}\n")
        mock.write(f"{problem['problem']}\n")
        mock.write(f"{' '.join(problem['choices'])}\n\n")
    mock.write("\\section{Answer Key}\n")
    for problem in mock_test:
        mock.write(f"{problem['number']}. {problem['answer']}\n")
    mock.write("\n\\section{Solutions}\n")
    for problem in mock_test:
        mock.write(f"\\subsection{{Problem {problem['number']}:}}\n")
        mock.write(f"{problem['solution']}\n\n")
