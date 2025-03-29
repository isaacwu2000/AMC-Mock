def generate_question(question_number, problems):
    # This is the problem distribution
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
    system = f"You generate math competition-style questions suitable for the AMC10 using the concept of {concept_distribution[question_number]}."
    system += " Your solutions must be CONCISE and EFFICIENT. Try NOT to use brute force or extremely long casework. "
    system += " Do NOT create geometry problems or problems requiring diagrams."
    system += " Provide the final answer explicitly as one of 'A', 'B', 'C', 'D', or 'E' EXACTLY."
    system += " Make sure to box your solution."
    system += " Write all mathematical expressions correctly in LaTeX, ensuring each expression starts with a \\."
    system += " Make sure there is only one slash, not two, when wriing LaTeX commands"
    system += " Present your solution clearly in bullet points using \\begin{itemize}, \\item, and \\end{itemize}."
    if question_number <= 5:
        system += "Make your problem easy, solvable by a somewhat mathematically inclined 10th grade school student."
    elif 5 < question_number <= 10:
        system += "Make your problems of medium-easy difficulty, solvable by a fairly clever 10th student."
    elif 10 < question_number <= 17:
        system += "Make your problem of medium-hard difficulty, solvable by an experienced 10th grade mathlete."
    elif 17 < question_number <= 25:
        system += "Make your problems of hard to very-hard difficulty, solvable by a highly clever and experienced 10th grade mathlete who is well practiced."
    system += f" Create problems of the EXACT SAME DIFFICULTY (ie. solution complexity) and style to the following examples:\n{example_problems}\n"
    
    prompt = f"Generate a problem {question_number} for the AMC10. The year is 2025, feel free to use that."

    # Inputting them into gemini and retunring the structured results
    from google import genai
    from google.genai import types
    from pydantic import BaseModel
    from dotenv import load_dotenv
    import os
    load_dotenv()

    # Creating a class for the problem gemini creates
    class Problem(BaseModel):
        problem: str
        solution: str
        answer: str
        choices: list[str]

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    generated_problem = client.models.generate_content(
        model="gemini-2.5-pro-exp-03-25", 
        config= types.GenerateContentConfig(
            response_mime_type = 'application/json',
            response_schema = list[Problem],
            system_instruction = system,
            temperature=1
        ),
        contents=prompt
    )
    # Convering the generated problem string into a dictionary
    import json
    generated_problem = json.loads(generated_problem.text)[0]
    # Adding the question number to the problem dictionary
    generated_problem["number"] = question_number 
    return generated_problem
