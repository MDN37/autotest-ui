# UI Course Automation Tests

This project implements automated tests for
the [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login). The
tests are written using **Python**, **Pytest**, **Allure** and **Playwright**. The test application’s source code is available
on [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Project Overview

The goal of this project is to automate the testing of the UI Course application. The automated tests verify various
functionalities of the application to ensure its stability and correctness. The project structure follows best practices
for organizing test code with clear, maintainable scripts.

## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/MDN37/autotest-ui.git
cd autotest-ui
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Additional Playwright Setup (if needed)

If you're running Playwright for the first time, you might need to install the required browsers:

```bash
playwright install
```

### Running the Tests with Allure Report Generation

To run regression tests and save Allure results, use:

```bash
python -m pytest -m "regression" --alluredir=./allure-results
```

To run the same suite in parallel (faster on multi-core machines):

```bash
python -m pytest -m "regression" --numprocesses=6 --dist=loadgroup
```

- `--numprocesses=6` — starts 6 worker processes
- `--dist=loadgroup` — keeps tests from the same group on one worker (avoids conflicts with shared resources)

### Viewing the Allure Report

Open an interactive Allure report in the browser:

```bash
allure serve ./allure-results
```

Generate a static single-file HTML report (easy to share or archive):

```bash
allure generate ./allure-results --clean -o ./chromium-webkit-firefox --single-file
```

- `--clean` — clears the output directory before generation
- `-o ./chromium-webkit-firefox` — output folder for the report
- `--single-file` — packs the report into one HTML file

### Code Style

Auto-format a file to PEP 8 (modifies the file in place):

```bash
autopep8 --in-place --aggressive --aggressive "fixtures/browsers.py"
```

- `--in-place` — writes changes to the same file
- `--aggressive` (twice) — applies more aggressive style fixes

Check a file for PEP 8 violations without changing it:

```bash
pycodestyle "fixtures/browsers.py"
```
