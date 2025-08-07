def generate_question(question_number, problems):
    # This is the problem distribution. There is not geometry because AI sucks at making diagrams and is inconsistent in solving
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

    # Getting the example problems in the bucket
    example_problems = ""
    for problem in problems[question_number]:
        example_problems += str(problem)

    # Setting the system and user prompts
    
    if question_number <= 5:
        system += "Make your problem easy, solvable by a somewhat mathematically inclined 10th grade school student."
    elif 5 < question_number <= 10:
        system += "Make your problems of medium-easy difficulty, solvable by a fairly clever 10th student."
    elif 10 < question_number <= 18:
        system += "Make your problem of medium-hard difficulty, solvable by an experienced 10th grade mathlete."
    elif 18 < question_number <= 25:
        system += "Make your problems of hard to very-hard difficulty, solvable by a highly clever and experienced 10th grade mathlete who is well practiced."
    system += f" Create problems of the EXACT SAME DIFFICULTY (ie. solution complexity) and style to the following examples:\n{example_problems}\n"
    prompt = f"Generate a problem {question_number} for the AMC10 (2026) on the topic of {concept_distribution[question_number]}"

    # Inputting them into gemini and retunring the structured results
    from dotenv import load_dotenv
    import os
    load_dotenv()

    # Creating a class for the problem gemini creates
    class Problem(BaseModel):
        problem: str
        solution: str
        answer: str
        choices: list[str]

    from openai import OpenAI
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5",
        input="Write a one-sentence bedtime story about a unicorn."
    )

    generated_problem = response.output_text

    # Convering the generated problem string into a dictionary
    import json
    generated_problem = json.loads(generated_problem)[0]
    # Adding the question number to the problem dictionary
    generated_problem["number"] = question_number 
    return generated_problem
