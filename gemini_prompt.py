import google.generativeai as genai
from datasets import load_dataset

dataset = load_dataset("openai_humaneval")

genai.configure(api_key="AIzaSyC9cnqwS1y8DUJkt0RLirFxHYG7KUCoL9I")

model = genai.GenerativeModel("gemini-2.0-flash")

for index in range(10):
    sample = dataset['test'][index]
    prompt = ("""You are a software engineer that is to only return 
                the code that will be generated according to this prompt. 
                Do not add any additional text.\n""" + sample['prompt'])
    response = model.generate_content(prompt)
    result = response.text