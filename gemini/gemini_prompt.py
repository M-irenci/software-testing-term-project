### @ Authors
### Stuudent Names: İsmail Can Karaağaç, Mahmutcan İrenci, Bahoz Yalçın
### Student IDs: 150210010, 150210034, 150210008


import json
from time import sleep
import google.generativeai as genai
from datasets import load_dataset

dataset = load_dataset("openai_humaneval")
genai.configure(api_key="AIzaSyC9cnqwS1y8DUJkt0RLirFxHYG7KUCoL9I")
model = genai.GenerativeModel("gemini-2.0-flash")

gemini_outputs: dict[int, dict[str, str]] = {}
chosen_test_prompts = {
    "easy": [32, 34, 38, 45, 50, 83, 162, 28, 29],
    "moderate": [33, 37, 42, 53, 59, 69, 90, 91, 94, 97],
    "hard": [40, 44, 48, 66, 67, 86, 95, 107, 109, 112, 128],
}

with open("manuel_unit_tests/prompts.json", "r", encoding="utf-8") as file:
    manuel_tests: dict[int, dict[str, str]] = json.load(file)

for test_count, difficulty in enumerate(chosen_test_prompts, 2):
    for index in chosen_test_prompts[difficulty]:
        sample = manuel_tests[str(index)]
        prompt = ("""You are a software engineer that is to only return 
                    the code that will be generated according to this prompt. 
                    Do not add any additional text.\n""" + sample['prompt'])
        response = model.generate_content(prompt)
        result_prompts = response.text

        test_prompt = f"""
            You are a software testing engineer.
            Generate {test_count} different unit tests for the function below
            Do not add any additional text:

            {result_prompts}
        """
        response = model.generate_content(test_prompt)
        result_tests = response.text

        gemini_outputs[index] = {
            "diff": difficulty,
            "result_prompts": result_prompts,
            "result_tests": result_tests,
        }

        sleep(9) # for api restrictions

with open("gemini/gemini_test_data.json", "w", encoding="utf-8") as file:
    json.dump(gemini_outputs, file, ensure_ascii=False, indent=2)
