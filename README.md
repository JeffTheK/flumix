# Flumix

A lisp like programming language

## Installation

* clone the repo
* cd into the cloned repo directory
* run `make install` or `pip install .`

## Usage

### Executing File

```sh
flumix PATH
```

where PATH is location of your source code file

### Syntax

#### Calling Functions

In flumix just like in lisp, functions are called in prefix notation,
where first comes the function name, and then the arguments.
For example, this program will sum two numbers:

```flumix
(+ 2 3)
```

#### Printing

```flumix
(print "Hello")
```

#### Variable Declaration

```flumix
(var i 5)
```

#### Function Declaration

```flumix
(func add (a b)
    (+ a b)
)
```