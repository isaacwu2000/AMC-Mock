# AMC-Mock
This project uses GPT-5 to generate a mock AMC10 with problems and solutin through context engineering, few-shot prompting (giving it example past AMC problems), and structured output.

## Example Mock
Download the pdf here: [AMC10_Mock_GPT_5.pdf](https://github.com/user-attachments/files/21675239/AMC10_Mock_GPT_5.1.pdf)

## Usage
You will need an OpenAI API key which you can obtain here: https://platform.openai.com/api-keys.

First, install the requirements:
```pip install requirements.txt```

Then, set your OpenAI API Key as an environemental variable:
```OPENAI_API_KEY = your-api-key-here```

Finally, in the terminal, run
```python main.py```
