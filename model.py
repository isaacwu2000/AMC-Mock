import json
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from prompt_setup import get_prompts

def generate_question(question_number, example_problems, previous_problems = []):
    prompt_info = get_prompts(question_number, example_problems, previous_problems = [])
    system, user, topic = prompt_info['system'], prompt_info['user'], prompt_info['topic']

    load_dotenv()
    client = OpenAI()

    class Problem(BaseModel):
        problem: str
        solution: str
        answer: str
        choices: list[str]

    response = client.responses.parse( # Todo: Set reasoning effort and verbostiy, use GPT-5 to otpimze prompt
        model="gpt-4.1-nano", # Todo: chagne back to GPT 5 after seeing it works
        instructions=system,
        input=user,
        text_format=Problem
    )

    generated_problem = response.output_parsed.model_dump()
    generated_problem["number"], generated_problem["topic"] = question_number, topic
    return generated_problem
