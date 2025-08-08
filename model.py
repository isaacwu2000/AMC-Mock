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

    response = client.responses.parse(
        model="gpt-5",
        instructions=system,
        input=user,
        text_format=Problem,
        reasoning={
            "effort": "high"
        }
    )

    generated_problem = response.output_parsed.model_dump()
    generated_problem["number"], generated_problem["topic"] = question_number, topic.split(",")[0]
    return generated_problem
