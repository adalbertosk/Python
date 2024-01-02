#! /usr/bin/python

import openai   
from bd import *

openai.api_key = api_key

#model_engine = "gpt-3.5-turbo" 
model_engine = "text-davinci-003"

prompt = "Hello, how are you today?"

completion = openai.completions.create(
    model=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)