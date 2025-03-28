def get_sorted_problems(json_file):
    # Getting and formatting the problems from the JSON file
    import json
    with open(json_file, 'r') as file:
        problems_json = json.load(file)

    problems = []
    for problem_set in problems_json:
        for problem in problem_set['problems']:
            problems.append(problem)

    # Soring the problems by problem number (an estimator for difficulty)
    problems.sort(key=lambda problem:problem["number"])

    # Outputing the sorted list of problems
    return problems

def divide_problem_buckets(problems):
    bucketed_problems = {}
    # Creating and filling the buckets
    for i in range(1, 26):
        bucketed_problems[i] = []
    for problem in problems:
        # The numbers 1-12 and 15, 18, 23 have only their singular number in the bucket
        if problem['number'] <= 12 or problem['number'] in [15, 18, 23]: 
            bucketed_problems[problem['number']].append(problem)
        # The numbers 13-14, 16-17, 19-20, 21-22, and 24-25 are double buckets
        elif problem['number'] in [13, 14]:
            bucketed_problems[13].append(problem)
            bucketed_problems[14].append(problem)
        elif problem['number'] in [16, 17]:
            bucketed_problems[16].append(problem)
            bucketed_problems[17].append(problem)
        elif problem['number'] in [19, 20]:
            bucketed_problems[19].append(problem)
            bucketed_problems[20].append(problem)
        elif problem['number'] in [21, 22]:
            bucketed_problems[21].append(problem)
            bucketed_problems[22].append(problem)
        elif problem['number'] in [24, 25]:
            bucketed_problems[24].append(problem)
            bucketed_problems[25].append(problem)
        # Raising an error if the problem number is invalid
        else:
            raise ValueError(f"Invalid problem number ({problem['number']})for {problem['problem']}")
    return bucketed_problems


