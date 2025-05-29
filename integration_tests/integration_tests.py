
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


Here is the first prompt for the first function:
{updated_prompts[prompt_indexes[0]]['prompt']}

Here is the second prompt for the second function:
{updated_prompts[prompt_indexes[1]]['prompt']}

Here is the third prompt for the third function:
{updated_prompts[prompt_indexes[2]]['prompt']}

---

You also need to implement a new function.
The fourth Python function called `rearrange_palindrome` that takes a string `s` and tries to rearrange its characters to form a palindrome.
You must use all three of the given methods to check if a string can be rearranged to become a palindrome in the fourth function.

If it's possible to rearrange the characters into a valid palindrome, return a tuple of the form `(palindrome_string, True)`, where `palindrome_string` is the rearranged palindrome.

If it's not possible to form a palindrome with the given characters, return `(None, False)`.

Additional requirements:
- The function must use `collections.Counter` to count character frequencies.
- At most one character may have an odd count in order for a palindrome to be possible.
- If a palindrome is possible, build it by placing the even-count characters symmetrically and the odd-count character (if any) in the middle.
- Use a helper function called `concatenate` to combine string parts.
- Use a helper function called `is_palindrome` to check if the final string is a valid palindrome.
- Do not use external libraries apart from Python standard library.
- Always use parentheses to avoid errors caused by process precedence

Class name should be `PalindromeOperations`.
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
