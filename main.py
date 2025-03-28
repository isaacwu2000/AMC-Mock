from manage_problems import get_sorted_problems, divide_problem_buckets
from model import generate_question

# Formatting the problems
non_bucketed_problems = get_sorted_problems('problems.json')
example_problems = divide_problem_buckets(non_bucketed_problems)
# Generating the mock test
mock_test = []
for i in range(1, 26):
    mock_test.append(generate_question(i, example_problems))
    print(mock_test)


# Writing it in latex to mock_text.txt
with open('mocks/mock_test.txt', 'w') as mock:
    mock.write("\\section*{Problems}")
    for problem in mock_test:
        mock.write(f"\\subsection*{{Problem {problem['number']}:}}")
        mock.write(f"{problem['problem']}\\\\\\\\")
        mock.write(f"{' '.join(problem['choices'])}\\\\")
    mock.write("\\pagebreak\\section*{Answer Key}")
    for problem in mock_test:
        mock.write(f"{problem['number']}. {problem['answer']}\\\\")
    mock.write("\\pagebreak\\section*{Solutions}")
    for problem in mock_test:
        mock.write(f"\\subsection*{{Problem {problem['number']}:}}")
        mock.write(f"{problem['solution']}")

