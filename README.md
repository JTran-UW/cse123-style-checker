# CSE 123 Style Checker
Automated Code Style Checker for UW CSE 123

This project requires Python 3.6+, Java 11, and NPM.

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

Open a new terminal, enter the frontend directory, and install and run the dev server

```
cd src/frontend

npm install

npm run dev
```

## Running unit tests

There is currently no suite for running all unit tests, so each chapter must be run separately.  Replace '2' with the appropriate chapter.

```
python -m unittest src.api.tests.CheckerTestsChapter2.py
```
