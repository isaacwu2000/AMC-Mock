# AMC-Mock
This project uses GPT-5 to generate a mock AMC10 through context engineering, few-shot prompting (giving it example past AMC problems), and structured output.

## Example Mock
<p align="center">
  <a href="https://amc10-mock-gpt-5.tiiny.site/">
    <img src="assets/demo.png" alt="AMC-10 Mock GPT-5 preview" width="700">
  </a>
</p>
Access pdf here: https://tiiny.host/manage.](https://amc10-mock-gpt-5.tiiny.site/

## Usage
You will need an OpenAI API key which you can obtain here: https://platform.openai.com/api-keys.

First, install the requirements:
```pip install requirements.txt```

Then, set your OpenAI API Key as an environemental variable:
```OPENAI_API_KEY = your-api-key-here```

Finally, in the terminal, run
```python main.py```
