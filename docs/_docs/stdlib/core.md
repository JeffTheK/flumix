---
title: "Core"
description: "Core functions and variables"
---

# Core

## Table

[`(do)`](#do)  [`(eval)`](#eval)  [`(func)`](#func)  [`(if)`](#if)  [`(include-file)`](#include-file)  [`(macro)`](#macro)  [`(pprint)`](#pprint)  [`(print)`](#print)  [`(set)`](#set)  [`(var)`](#var)  
## `(do statements...)`
<a id="do"></a>
```
Executes all statements
```
<br>
## `(eval statements...)`
<a id="eval"></a>
```
Evaluates all statements
```
<br>
## `(func name (params...) body...)`
<a id="func"></a>
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
## `(if condition on-true on-false)`
<a id="if"></a>
```
If statement
```
<br>
## `(include-file path)`
<a id="include-file"></a>
```
Loads source code file from local path or stdlib package
```
<br>
## `(macro name (params...) body...)`
<a id="macro"></a>
```
Defines a new macro
```
<br>
## `(pprint args...)`
<a id="pprint"></a>
```
Outputs values with pretty formatting
```
<br>
## `(print args...)`
<a id="print"></a>
```
Outputs arguments
```
<br>
## `(set symbol new-value)`
<a id="set"></a>
```
Modifies an existing variable
```
<br>
## `(var name value)`
<a id="var"></a>
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
