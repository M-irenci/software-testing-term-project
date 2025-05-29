
# Software Testing Term Project

## Project Overview

This project involves automated testing of different AI models (Gemini and LLaMA). The primary objective is to create and run tests dynamically on models, evaluate their correctness, and compute success ratios. The output for these models stored in two primary directories, **gemini** and **llama**, which contain different scripts and JSON data files. 

Manual tests and a sample integration between such prompts are also given in directories of **manuel_unit_tests** and **integration_tests**.

## Project Structure

```plaintext
SOFTWARE-TESTING-TERM-PROJECT
│
├── gemini/
│   ├── gemini_prompt.py                    # Prompt generation for Gemini
│   ├── gemini_success_ratios.json          # Stores success ratios for Gemini model
│   ├── gemini_test_data.json               # Test data for Gemini models
│   ├── gemini_test_results.txt             # Test output for Gemini models
│   └── test_gemini_data.py                 # Testing scripts for Gemini model
│
├── llama/
│   ├── llama_prompt.py                     # Prompt generation for LLaMA
│   ├── llama_success_ratios.json           # Stores success ratios for LLaMA model
│   ├── llama_test_data.json                # Test data for LLaMA models
│   ├── llama_test_results.txt              # Test output for LLaMA models
│   └── test_llama_data.py                  # Testing scripts for LLaMA model
│
├── manuel_unit_tests/
│   ├── extract_prompts.py                  # Print prompts in a processable way
│   ├── gemini_manuel_success_ratios.json   # Updated success of Gemini model
│   ├── gemini_manuel_test_results.txt      # Printout of outputs
│   ├── gemini_test_manuel_tests.py         # Function that executes tests
│   ├── llama_manuel_success_ratios.json    # Updated success of LLaMA model
│   ├── llama_manuel_test_results.txt       # Printout of outputs
│   ├── llama_test_manuel_tests.py          # Function that executes tests
│   ├── prompts_gemini.json                 # Edited prompts for Gemini
│   └── prompts_llama.json                  # Edited prompts for LLaMA
│
├── integration_tests/
│   ├── gemini_response.py                  # Resulting class from integration_tests.py
│   ├── integration_tests.py                # Function that prompts models with class request
│   ├── llama_response.py                   # Resulting class from integration_tests.py
│   └── manuel_tests.py                     # Tests that we wrote
│
└── README.md                               # Project documentation
```

## Models Explanation

- **gemini/**: Contains all files related to Gemini AI models. The `gemini_test_data.json` includes the data to be tested, and the `gemini_success_ratios.json` stores the results (success ratio for each function).
- **llama/**: Contains files related to LLaMA AI models, with similar data structure as **gemini/**.
- **gemini_prompt.py** and **llama_prompt.py**: These files contain api calls and fixed prompt contents to create functions and related unit tests for each case.
- **test_gemini_data.py** and **test_llama_data.py**: These Python files contain the logic to load the test data, execute the tests, and capture results.
- **gemini_test_results.txt** and **llama_test_results.txt**: Files containing the output from running the tests for each AI model.

## How to Run

1. Make sure all dependencies are installed and keys are up to date.
2. Run the appropriate test script for either Gemini or LLaMA, or the integration test:
    - `python test_gemini_data.py` for Gemini tests.
    - `python test_llama_data.py` for LLaMA tests.
    - `integration_tests.py ` for LLaMA tests.

OR 
   Run `python gemini_prompt.py` or `python llama_prompt.py` and then run their respective `python gemini_test_manuel_tests.py` or `python llama_test_manuel_tests.py` for phase 2 versions.
3. The results will be saved in the `.json` files.


## Notes

1. For both models, free tier APIs are used. Results may vary with paid advanced models. "gemini-2.0-flash" and "llama3-70b-8192" models are used respectively.
