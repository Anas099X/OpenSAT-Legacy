from g4f.client import Client
import g4f
from insert_questions import add_question
from PyPDF2 import PdfReader
import time
import google.generativeai as genai
import os


client = Client()
reader = PdfReader("main_input.pdf")


#import prompt for instuctions
promptfile = open("question generator/reformat_prompt.txt", "r+").read()

#importfile = open("input.txt", "r+")
outputfile = open("internal_db/SAT_database.json", "w+")

#auto question converter and exporter
sat_pdf = reader.pages
for page in sat_pdf:
 genai.configure(api_key='AIzaSyAhQgVvkqgJDqY470q9bR-5p0EW4G3NCS0')

 model = genai.GenerativeModel('gemini-1.0-pro-latest')
 response = model.generate_content(promptfile + "\n" + page.extract_text())
 try:
  add_question("sat_database","english",response.text)
  outputfile.write(response.text + ',')
  time.sleep(0.55)
  print("Question Added!")
  print(response.text)
 except:
  print("Skipped for invalid input or output")  

