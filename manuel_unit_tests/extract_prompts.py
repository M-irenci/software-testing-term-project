### @ Authors
### Stuudent Names: İsmail Can Karaağaç, Mahmutcan İrenci, Bahoz Yalçın
### Student IDs: 150210010, 150210034, 150210008


import json
from datasets import load_dataset

dataset = load_dataset("openai_humaneval")

prompts: dict[int, dict[str, str]] = {}
chosen_test_prompts = {
    "easy": [32, 34, 38, 45, 50, 83, 162, 28, 29],
    "moderate": [33, 37, 42, 53, 59, 69, 90, 91, 94, 97],
    "hard": [40, 44, 48, 66, 67, 86, 95, 107, 109, 112, 128],
}

for test_count, difficulty in enumerate(chosen_test_prompts, 2):
    for index in chosen_test_prompts[difficulty]:
        sample = dataset['test'][index]
        prompts[index] = {
            "diff": difficulty,
            "prompt": sample['prompt'],
        }

with open("manuel_unit_tests/prompts.json", "w", encoding="utf-8") as file:
    json.dump(prompts, file, ensure_ascii=False, indent=2)
