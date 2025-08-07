import json
from pydantic import BaseModel
from openai import OpenAI
from prompt_setup import get_prompts

def generate_question(question_number, example_problems, previous_problems = []):
    prompts = get_prompts(question_number, example_problems, previous_problems = [])
    system, user = prompts['system'], prompts['user']

    load_dotenv()
    client = OpenAI()

    class Problem(BaseModel):
        problem: str
        solution: str
        answer: str
        choices: list[str]
        concepts: list[str]

    response = client.responses.create( # Todo: Set reasoning effort and verbostiy, use GPT-5 to otpimze prompt
        model="gpt-4.1-nano", # Todo: chagne back to GPT 5 after seeing it works
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        text_format=Problem
    )

    generated_problem = response.output_parsed
    generated_problem = generated_problem[0]
    generated_problem["number"] = question_number 
    return generated_problem
