# dailyprogrammer

[![Travis branch](https://img.shields.io/travis/tommilligan/dailyprogrammer/develop.svg)](https://travis-ci.org/tommilligan/dailyprogrammer)
[![codecov](https://codecov.io/gh/tommilligan/dailyprogrammer/branch/develop/graph/badge.svg)](https://codecov.io/gh/tommilligan/dailyprogrammer)
[![Requires.io](https://img.shields.io/requires/github/tommilligan/dailyprogrammer.svg)](https://requires.io/github/tommilligan/dailyprogrammer/requirements/?branch=master)
[![license](https://img.shields.io/github/license/tommilligan/dailyprogrammer.svg)]()


## Installation

Clone and install using pip
```
git clone git@github.com:tommilligan/dailyprogrammer
pip install ./dailyprogrammer
```

## New challanges

New challenges can be added in a modular format by creading a new submodule under `dailyprogrammer.challanges`, with a `main` function that accepts a string as input.

```python
# dailyprogrammer/challanges/<challange_name>/__init__.py

def main(inputString):
    # do challange <challange_name>!
    return outputString
```

This function will be automagically imported and called by the cli.

```bash
dailyprogrammer <challenge_name> <challange_input>
```

Tests should be mirror-added to the top level `test` module.

## Development

Install with
```
pip install -e ./dailyprogrammer
pip install -r requirements-dev.txt
```

Development tasks
```
# Test and cover
nose2 --with-coverage --coverage-report html
```
