
# Software Testing Term Project

## Project Overview

This project involves automated testing of different AI models (Gemini and LLaMA). The primary objective is to create and run tests dynamically on models, evaluate their correctness, and compute success ratios. The outpu for these models stored in two primary directories, **gemini** and **llama**, which contain different scripts and JSON data files.

## Project Structure

```plaintext
SOFTWARE-TESTING-TERM-PROJECT
│
├── gemini/
│   ├── gemini_prompt.py           # Prompt generation for Gemini
│   ├── gemini_success_ratios.json # Stores success ratios for Gemini model
│   ├── gemini_test_data.json     # Test data for Gemini models
│   ├── gemini_test_results.txt   # Test output for Gemini models
│   └── test_gemini_data.py       # Testing scripts for Gemini model
│
├── llama/
│   ├── llama_prompt.py           # Prompt generation for LLaMA
│   ├── llama_success_ratios.json # Stores success ratios for LLaMA model
│   ├── llama_test_data.json      # Test data for LLaMA models
│   ├── llama_test_results.txt    # Test output for LLaMA models
│   └── test_llama_data.py        # Testing scripts for LLaMA model
│
└── README.md                     # Project documentation
```

## Models Explanation

- **gemini/**: Contains all files related to Gemini AI models. The `gemini_test_data.json` includes the data to be tested, and the `gemini_success_ratios.json` stores the results (success ratio for each function).
- **llama/**: Contains files related to LLaMA AI models, with similar data structure as **gemini/**.
- **gemini_prompt.py** and **llama_prompt.py**: These files contain api calls and fixed prompt contents to create functions and related unit tests for each case.
- **test_gemini_data.py** and **test_llama_data.py**: These Python files contain the logic to load the test data, execute the tests, and capture results.
- **gemini_test_results.txt** and **llama_test_results.txt**: Files containing the output from running the tests for each AI model.

## How to Run

1. Make sure all dependencies are installed.
2. Run the appropriate test script for either Gemini or LLaMA:
    - `python test_gemini_data.py` for Gemini tests.
    - `python test_llama_data.py` for LLaMA tests.
3. The results will be saved in the `.json` files.


## Notes

1. For both models, free tier APIs are used. Results may vary with paid advanced models.