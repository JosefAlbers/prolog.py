# Prolog Interpreter in Python

Minimal implementation of a Prolog interpreter in 86 lines of Python.

## Features

* Parses Prolog rules and queries
* Executes queries using a depth-first search algorithm
* Supports unification of terms
* Allows for recursive rules

## Usage

To use the interpreter, simply run the `prolog.py` file and enter Prolog queries or rules at the prompt. For example:

```bash
% python prolog.py
: boy(joe)
: boy(joe)?
```

This will execute the query `boy(joe)` and print the results.

You can also pass a string of prompts to the `prolog` function, like this:

```python
from prolog import prolog

prompts = """
parent(ann,liz)
parent(jon,ann)
grandparent(X,Z):-parent(X,Y),parent(Y,Z)
grandparent(jon,liz)?

boy(uri)
mother(ola,uri)
mother(ola,gil)
father(yan,uri)
father(ned,gil)
mother(X,uri)?
mother(ola,Y)?

child(X,Y):-mother(Y,X)
child(X,Y):-father(Y,X)
son(X,Y):-child(X,Y),boy(X)
son(uri,Z)?
son(I,J)?

sibling(X,Y):-mother(Z,X),mother(Z,Y)
sibling(uri,gil)?
"""

prolog(prompts)

# Output:
# boy(joe)? -> [True]
# grandparent(jon,liz)? -> [True]
# mother(X,uri)? -> [{'X': 'ola'}]
# mother(ola,Y)? -> [{'Y': 'gil'}, {'Y': 'uri'}]
# son(uri,Z)? -> [{'Z': 'yan'}, {'Z': 'ola'}]
# son(I,J)? -> [{'I': 'uri', 'J': 'yan'}, {'I': 'uri', 'J': 'ola'}]
# sibling(uri,gil)? -> [True]
```

This will execute the queries and rules in the prompt string.

## Code Structure

The code is organized into several classes and functions:

* `Term`: represents a Prolog term, with a predicate and a list of arguments
* `Rule`: represents a Prolog rule, with a head and a list of goals
* `Goal`: represents a Prolog goal, with a rule and a dict of atoms
* `unify`: unifies two terms and returns a new dict of atoms
* `search`: executes a query using a depth-first search algorithm
* `solve`: parses a Prolog query or rule and executes it
* `prolog`: runs the interpreter and executes queries or rules