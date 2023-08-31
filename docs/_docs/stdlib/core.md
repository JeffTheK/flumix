---
title: "Core"
description: "Core functions and variables"
---

# Core

## `(do statements...)`

```
Executes all statements
```
<br>
## `(var name value)`

```
Defines a new variable
```
##### Example
```lisp
(do
    (var i 5)
    (print i)
)
--> 5

```
<br>
## `(set symbol new-value)`

```
Modifies an existing variable
```
<br>
## `(func name (params...) body...)`

```
Defines a new function
```
##### Example
```lisp
(do
    (func my-add (a b)
        (+ a b)
    )

    (print (my-add 2 3))
)
--> 5

```
<br>
## `(macro name (params...) body...)`

```
Defines a new macro
```
<br>
## `(eval statements...)`

```
Evaluates all statements
```
<br>
## `(print args...)`

```
Outputs arguments
```
<br>
## `(pprint args...)`

```
Outputs values with pretty formatting
```
<br>
## `(if condition on-true on-false)`

```
If statement
```
<br>
## `(include-file path)`

```
Loads source code file from local path or stdlib package
```
<br>
