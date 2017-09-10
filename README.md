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

## Currently solved challenges

* `c20170811h0` [[2017-08-11] Challenge #326 [Hard] Multifaceted alphabet blocks](notes/c20170811h0/notes.md)
* `c20170811h0` [2017-09-04] Challenge #330 [Easy] Surround the circles
    * `c20170811h2` [extension that finds the optimal orientation for a bounding box](notes/c20170904h2/notes.md)

## New challanges

New challenges can be added in a modular format by creading a new submodule under `dailyprogrammer.challanges`, with a `main` function that accepts and returns a string.

```python
# dailyprogrammer/challanges/<challange_name>/__init__.py

def main(challengeInput):
    challengeOutput = someComplexFunction(challengeInput)
    return challengeOutput
```

This function will be automagically imported and called by the command line interface.

Implemented challenges can be listed with `dailyprogrammer --list`.

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
