def generate_question(question_number, problems):
    # Getting the example problems in the bucket
    example_problems = ""
    for problem in problems[question_number]:
        example_problems += str(problem)

    # Setting the system and user prompts
    system = "You generate math competition-style questions suitable for the AMC10."
    system += " Your solutions must be CONCISE and EFFICIENT. Try NOT to use brute force or extremely long casework. "
    system += " Do NOT create geometry problems or problems requiring diagrams."
    system += " Write all mathematical expressions correctly in LaTeX, ensuring each expression starts with a \\."
    system += " Make sure there is only one slash, not two, when wriing LaTeX commands"
    system += " Present your solution clearly in bullet points using \\begin{itemize}, \\item, and \\end{itemize}."
    system += " Provide the final answer explicitly as one of 'A', 'B', 'C', 'D', or 'E' EXACTLY."
    system += f" Create problems similar in DIFFICULTY (ie. solution complexity) and style to the following examples:\n{example_problems}"

    prompt = "Generate one problem for the AMC10. The year is 2025, feel free to use that."

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
        choices: list[str]
        solution: str
        answer: str

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
