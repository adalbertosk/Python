import os
from bd import api_key
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = api_key
llm = OpenAI(model_name="text-davinci-003")
"""
print(llm("explain large language models in one sentence"))

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
messages = [
    SystemMessage(content="You are an expert data scientist"),
    HumanMessage(content="Write a python script that trains a neural network on simulated data")
]
response=chat(messages)
print(response.content,end='\n')
"""
from langchain.prompts import PromptTemplate
template = """
You are an expert data scientist with an expertise in building deep learning models.
Explain the concept of {concept} in a couple of lines
"""

prompt = PromptTemplate(
    input_variables=["concept"],
    template=template
)
#print(llm(prompt.format(concept="regularization")))

from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

#print(chain.run("autoencoder"))

second_prompt = PromptTemplate(
    input_variables=["ml_concept"],
    template="Turn the concept description of {ml_concept} and explain it to me like I'm five",
)
chain_two = LLMChain(llm=llm, prompt=second_prompt)

from langchain.chains import SimpleSequentialChain
overall_chain = SimpleSequentialChain(chains=[chain, chain_two], verbose=True)
explanation = overall_chain.run("autoencoder")
print(explanation)