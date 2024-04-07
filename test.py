from g4f.client import Client
from PyPDF2 import PdfReader

client = Client()
reader = PdfReader("test.pdf")

def send_message(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

page = reader.pages
for i in page:
    message = f"turn following text into json: {i}"
    response = send_message(message)
    print(f"Response: {response}")