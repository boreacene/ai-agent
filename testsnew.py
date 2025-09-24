from functions.get_files_info import get_files_info

test_cases = (
    {
        "working_dir": "calculator",
        "directory": ".",
        "label": "Result of current directory:",
        "expected_lines": [
            "- main.py: file_size=<N>, is_dir=False",
            "- tests.py: file_size=<N>, is_dir=False",
            "- pkg: file_size=<N>, is_dir=True",
        ],
    },
    {
        "working_dir": "calculator",
        "directory": "pkg",
        "label": "Result of current directory:",
        "expected_lines": [
            "- calculator.py: file_size=<N>, is_dir=False",
            "- render.py: file_size=<N>, is_dir=False",
        ],
    },
    {
        "working_dir": "calculator",
        "directory": "/bin",
        "label": "Result of current directory:",
        "expected_lines": 'Error: Cannot list "/bin" as it is outside the permitted working directory',
    },
    {
        "working_dir": "calculator",
        "directory": "../",
        "label": "Result of current directory:",
        "expected_lines": 'Error: Cannot list "../" as it is outside the permitted working directory',
    },
)
