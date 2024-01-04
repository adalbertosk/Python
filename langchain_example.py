import os
import sys
from bd import api_key

from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import OnlinePDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from fpdf import FPDF

os.environ["OPENAI_API_KEY"] = api_key

query = "Describe the place I work"

#loader = TextLoader('data.txt') 
loader = DirectoryLoader("datasources/")
#loader = PyPDFLoader("Beacon-Hospital.pdf")
#loader = PyPDFLoader("https://showme.co.za/george/files/2017/07/McDonalds.pdf", extract_images=True)
#loader = OnlinePDFLoader("https://showme.co.za/george/files/2017/07/McDonalds.pdf")
index = VectorstoreIndexCreator().from_loaders([loader])

#print(index.query(query))
#print(index.query(query, llm=ChatOpenAI()))

pdf = FPDF()
text = index.query(query)
pdf.add_page()
pdf.set_font('Arial', size=12)
pdf.write(5, text)
pdf.output('output.pdf')