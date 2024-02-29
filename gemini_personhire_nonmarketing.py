import json
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

from IPython.display import Markdown
import textwrap

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

safety_settings=[
  {
    "category": "HARM_CATEGORY_DANGEROUS",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    safety_settings=safety_settings
)

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def personhire_nonmarketing_response(input):
  
    prompt = f"""You are an article analyst who analyses marketing activity and extracts key information that is requested of you.\
    Please read the given article text and answer the questions below.\
    Note: Please give the response in JSON format with proper indentation for better user readability.\
    The field names for the JSON are as follows:\
    ""Company Name"", ""Company Domain Name"", ""New Hire"", ""Job title"", ""Previous Workplace", ""Aim of Company with New Hire"", ""Geography"".\
    Rules for JSON fields:\
    ""Company Name"": Which company is the text talking about?\
    ""Company Domain Name"": Please return the website link for the company mentioned above.\
    ""New Hire"": Who is the new hire?\
    ""Job Title"": What is their job title?\
    ""Previous Workplace"": Where did the person work previously?\
    ""Aim of Company with  New Hire"": What is the future aim of the company with this new hire/role? (e.g. to drive growth, to bring the brand to new audiences, etc)\
    ""Geography"": What geographies are mentioned?\
    If for any of the above questions the answer is not present in the text then return "Not Specified".\
    text :  ```{input}```\
    """
    response = model.generate_content(str(prompt))
    # to_markdown(response.text)
    
    return response.text

