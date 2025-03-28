def general_gemini(prompt = "", system = "", temp = 1):
    from google import genai
    from google.genai import types
    from dotenv import load_dotenv
    import os
    load_dotenv()

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.5-pro-exp-03-25", 
        config= types.GenerateContentConfig(
            system_instruction = system,
            temperature=temp
        ),
        contents=prompt
    )
    return response.text

def generate_question(question_number, problems):
    # Getting the example problems in the bucket
    example_problems = ""
    for problem in problems[question_number]:
        example_problems += str(problem)

    # Setting the system and user prompts
    system = "You generate math competition style questions for the AMC10. "
    system += "Your solutions should be CONCISE and EFFICIENT. "
    system += "You do not make geometry problems or any type of problem that involves a diagram. "
    system += "You write everything in LaTex. "
    system += "Your answer should be 'A', 'B', 'C', or 'D' EXACTLY. "
    system += f"You make problems of similar difficulty and style to the following:\n{example_problems}"
    prompt = f"Generate a problem for the AMC10."

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
