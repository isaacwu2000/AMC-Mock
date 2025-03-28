from manage_problems import get_sorted_problems, divide_problem_buckets
non_bucketed_problems = get_sorted_problems('problems.json')
problems = divide_problem_buckets(non_bucketed_problems)


