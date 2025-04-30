### @ Authors
### Stuudent Names: İsmail Can Karaağaç, Mahmutcan İrenci, Bahoz Yalçın
### Student IDs: 150210010, 150210034, 150210008


import os
import json
from groq import Groq
from time import sleep
from datasets import load_dataset


def generate_content(system_prompt: str, user_prompt: str):
    chat_completion = client.chat.completions.create(
        temperature=0.2,
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
    )

    response = chat_completion.choices[0].message.content
    return response


dataset = load_dataset("openai_humaneval")
client = Groq(api_key="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")

llama_outputs: dict[int, dict[str, str]] = {}
chosen_test_prompts = {
    "easy": [32, 34, 38, 45, 50, 83, 162, 28, 29],
    "moderate": [33, 37, 42, 53, 59, 69, 90, 91, 94, 97],
    "hard": [40, 44, 48, 66, 67, 86, 95, 107, 109, 112, 128],
}
for test_count, difficulty in enumerate(chosen_test_prompts, 2):
    for index in chosen_test_prompts[difficulty]:
        sample = dataset['test'][index]
        prompt = (
            "You are a software engineer",
            """Only return the code that will be generated according to this prompt. 
                Do not add any additional text.\n""" + sample['prompt'])
        result_prompts = generate_content(*prompt)

        test_prompt = (
            "You should give test cases for the given functions by following the restrictions.",
            f"""Generate {test_count} different unit tests for the function below
            Give tests as seperate classess, not as functions;
            Always import necessary libraries at the top of the each class, but dont import the function you are testing;
            Do not add any additional text, neither on the top nor the bottom.
            only put "*****" between the classes, so that I can split them, consider syntax and indentation for each split and make sure that the code is executable;
            Do not add anything else other than the imports and classes:

            {result_prompts}
        """)
        result_tests = generate_content(*test_prompt)
        print(result_tests)
        llama_outputs[index] = {
            "diff": difficulty,
            "result_prompts": result_prompts,
            "result_tests": result_tests,
        }

        sleep(5) # for api restrictions

with open("llama_test_data.json", "w", encoding="utf-8") as file:
    json.dump(llama_outputs, file, ensure_ascii=False, indent=2)
