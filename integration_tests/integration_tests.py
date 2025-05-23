
### @ Authors
### Student Names: İsmail Can Karaağaç, Mahmutcan İrenci, Bahoz Yalçın
### Student IDs: 150210010, 150210034, 150210008


import json
import google.generativeai as genai
from groq import Groq

genai.configure(api_key="AIzaSyC9cnqwS1y8DUJkt0RLirFxHYG7KUCoL9I")
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

llama_client = Groq(api_key="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")

def generate_llama(system_prompt: str, user_prompt: str):
    chat_completion = llama_client.chat.completions.create(
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


with open("manuel_unit_tests/prompts_gemini.json", "r", encoding="utf-8") as file:
    updated_prompts: dict[int, dict[str, str]] = json.load(file)

prompt_indexes = ["28", "48", "112"]
prompt_text = f"""

You will be given 3 different prompts. Each prompt will be a different function that you need to implement.
You need to implement a class that will have these three functions.
The third function needs to call the second function in the end.
You also need to implement a new function.
The new function must use all three of the given methods to check if a string can be rearranged to become a palindrome.
The new function should take a string, remove the characters that prevent it from being a palindrome, use concatenate function to attach front and back of output string until a palindrome is obtained.
Make sure a character has attached that many times to the front and back of the string, since remove_delete all instances of the character.
The new function will be called `rearrange_palindrome`.
The new function will get a string to rearrange. If the function has more than one odd character count, it will return None.
The new function will return the result palindrome, None if there isn't an output and a boolean to show the output for tests.
Make sure to use all three of the given methods to check if a string can be rearranged to become a palindrome.
Make sure odd characters are in the middle of the string.

Here is the first prompt for the first function:
{updated_prompts[prompt_indexes[0]]['prompt']}

Here is the second prompt for the second function:
{updated_prompts[prompt_indexes[1]]['prompt']}

Here is the third prompt for the third function:
{updated_prompts[prompt_indexes[2]]['prompt']}

You need to implement a class that will have these three functions and the fourth function as described.


You need to write a class that will have the functions concatenate, is_palindrome reverse_delete that are explained above.
You must use all three of the given methods to check if a string can be rearranged to become a palindrome in the fourth new function.
"""

# Save Gemini response
gemini_response = gemini_model.generate_content(prompt_text)
gemini_test_response = gemini_model.generate_content(
    f"Write 5 integration tests only for the last method of the following class, just give the test class, do not give anthing else: {gemini_response.text}"
)

with open("integration_tests/gemini_response.py", "w", encoding="utf-8") as file:
    file.write(gemini_response.text + "\n" + gemini_test_response.text)

llama_response = generate_llama("""You are a software engineer that is to only return 
                    the code that will be generated according to this prompt. 
                    Do not add any additional text.\n""", prompt_text)
llama_test_response = generate_llama(
    """You are a software engineer that is to only return 
                    the code that will be generated according to this prompt. 
                    Do not add any additional text.\n""",
    f"Write 5 integration tests only for the last method of the following class, just give the test class, do not give anthing else: {llama_response}"
)

with open("integration_tests/llama_response.py", "w", encoding="utf-8") as file:
    file.write(llama_response + "\n" + llama_test_response)
