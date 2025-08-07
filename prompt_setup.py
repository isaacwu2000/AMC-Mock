def get_prompts(question_number, example_problems, previous_problems = []):
    # There is no geometry or diagrams because AI sucks at making diagrams
    # and is inconsistent in solving problems with them
    concept_distribution = {
        1: "Algebra",
        2: "Algebra",
        3: "Number Theory",
        4: "Number Theory",
        5: "Number Theory",
        6: "Counting and Probability",
        7: "Number Theory",
        8: "Counting and Probability",
        9: "Counting and Probability",
        10: "Number Theory",
        11: "Number Theory",
        12: "Algebra",
        13: "Algebra",
        14: "Counting and Probability",
        15: "Number Theory",
        16: "Algebra",
        17: "Counting and Probability",
        18: "Number Theory",
        19: "Algebra",
        20: "Counting and Probability",
        21: "Algebra",
        22: "Algebra",
        23: "Algebra",
        24: "Counting and Probability",
        25: "Algebra"
    }
    
    with open("system_prompt.txt") as f:
        system_prompt = f.read()

    if previous_problems: 
        system_prompt += "\n\n# Previous problems:"
        for i in range(len(previous_problems)):
            system_prompt += f"\n{str(i)}. {previous_problems[i]}"

    system_prompt += "\n\n# Examples problems:"
    for example_problem in example_problems[question_number]:
        system_prompt += "\n" + str(example_problem)

    user_prompt = f"Create a problem {question_number} for the AMC10 (2026) on the topic of {concept_distribution[question_number]}."
    
    return {"system":system_prompt, "user":user_prompt, "topic":{concept_distribution[question_number]}}