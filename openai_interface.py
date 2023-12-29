```python
# openai_interface.py

import openai
from config import OPENAI_API_KEY

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_text(prompt, max_tokens=100):
    """
    Function to generate text using OpenAI's GPT-3 model.
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens
    )

    return response.choices[0].text.strip()
```
