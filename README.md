# cse123-style-checker
Automated Code Style Checker for UW CSE 123

This project requires Python 3.6+ and Java 11.

## Getting started

Update and build the checkstyle submodule

```
git pull

git submodule update --init --recursive

cd checkstyle

mvn install
```

The appropriate jar file should be found in the target subdirectory.
