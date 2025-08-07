def generate_question(question_number, problems):
    
    user_prompt = f"Create a problem {question_number} for the AMC10 (2026) on the topic of {concept_distribution[question_number]}."


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
