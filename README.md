# AMC-Mock
This project uses GPT-5 to generate a mock AMC10 through context engineering, few-shot prompting (giving it example past AMC problems), and structured output.

## Example Mock
<img width="857" height="697" alt="AMC_Mock_GPT-5" src="https://github.com/user-attachments/assets/c6b75be7-8949-4814-be60-367563c11a8d" />
Access pdf here: https://tiiny.host/manage.

## Usage
You will need an OpenAI API key which you can obtain here: https://platform.openai.com/api-keys.

First, install the requirements:
```pip install requirements.txt```

Then, set your OpenAI API Key as an environemental variable:
```OPENAI_API_KEY = your-api-key-here```

Finally, in the terminal, run
```python main.py```
