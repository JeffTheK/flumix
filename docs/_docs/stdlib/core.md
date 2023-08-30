---
title: Core
description: Core functions and variables
---

# Core

### print

```lisp
(print args...)
```

Outputs all arguments

### var

```lisp
(var name value)
```

Defines a new variable

### do

```lisp
(do statements...)
```

Executes all statements

### set

```lisp
(set variable value)
```

Overrides variable with new value

### func

```lisp
(func name (parameters...)
    statements...
)
```

Defines a new function

### macro

```lisp
(macro name (parameters...)
    statements...
)
```

Defines a new macro. The difference between a function and a macro is
that when calling a function, all parameters are evaluated by default,
where as in macros, they are not

### eval

```lisp
(eval args...)
```

Evaluates arguments

### include-file

```lisp
(include-file path)
```

Loads a file from relative path or from stdlib package

### if

```lisp
(if condition
    on-true
    on-false
)
```

If statement