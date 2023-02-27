# cse123-style-checker
Automated Code Style Checker for UW CSE 123

This project requires Python 3.6+ and Java 11.

## Getting started

Update and build the checkstyle submodule

```
cd checkstyle

git pull

git submodule update --init --recursive

cd ..

mvn clean package -Passembly,no-validations
```

Open a new virtual Python environment and install required packages

```
python -m venv venv

source bin/venv/activate

pip install -r requirements.txt
```

Run the API

```
uvicorn src.api.checkstyle:app --reload
```

Access the web app @ 'src/frontend/index.html'

## Running unit tests

There is currently no suite for running all unit tests, so each chapter must be run separately.  Replace '2' with the appropriate chapter.

```
python -m unittest tests.CheckerTestsChapter2.py
```
