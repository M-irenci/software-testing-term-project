### @ Authors
### Stuudent Names: İsmail Can Karaağaç, Mahmutcan İrenci, Bahoz Yalçın
### Student IDs: 150210010, 150210034, 150210008


import re
import json
import unittest
import io
from contextlib import redirect_stdout, redirect_stderr

with open("llama_test_data.json", "r", encoding="utf-8") as file:
    llama_outputs: dict[int, dict[str, str]] = json.load(file)

test_results = {}
success_ratios = {}
for index, data in llama_outputs.items():
    try:
        local_env = {}
        code_blocks = [data["result_prompts"]] + data["result_tests"].split("*****")

        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer), redirect_stderr(output_buffer):
            for block in code_blocks:
                exec(block, local_env)

            suite = unittest.defaultTestLoader.loadTestsFromModule(type("FakeModule", (), local_env))
            result = unittest.TextTestRunner(stream=output_buffer, verbosity=2).run(suite)
            test_results[index] = output_buffer.getvalue()

        # Compute success ratio
        total = result.testsRun
        failed = len(result.failures) + len(result.errors)
        passed = total - failed
        ratio = passed / total if total > 0 else 0.0

        success_ratios[index] = {
            "total": total,
            "passed": passed,
            "failed": failed,
            "success_ratio": ratio
        }
        print(f"Test case {index} completed with success ratio: {success_ratios[index]['success_ratio']}")

    except Exception as e:
        success_ratios[index] = {
            "error": str(e),
            "success_ratio": 0.0
        }

with open("llama_test_results.txt", "w", encoding="utf-8") as file:
    for idx, out in test_results.items():
        file.write(f"--- Test Case {idx} ---\n{out}\n")

with open("llama_success_ratios.json", "w", encoding="utf-8") as file:
    json.dump(success_ratios, file, ensure_ascii=False, indent=2)
