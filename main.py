from g4f.client import Client
from insert_questions import add_question
from PyPDF2 import PdfReader

reader = PdfReader("test.pdf")
page = reader.pages[0]

promptfile = open("prompt_input.txt", "r+")
importfile = open("input.txt", "r+")
outputfile = open("output.json", "w+")

client = Client()
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": promptfile.read() + "\n" + page.extract_text()}],
    
)
outputfile.write(response.choices[0].message.content)
add_question("sat_question_test","questions",response.choices[0].message.content)
#print(response.choices[0].message.content)

