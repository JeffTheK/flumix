---
title: "Core"
description: "Core functions and variables"
---

# Core

## Table

[`(do)`](#do)  [`(var)`](#var)  [`(set)`](#set)  [`(func)`](#func)  [`(macro)`](#macro)  [`(eval)`](#eval)  [`(print)`](#print)  [`(pprint)`](#pprint)  [`(if)`](#if)  [`(include-file)`](#include-file)  
## `(do statements...)`
<a id="do"></a>
```
Executes all statements
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
## `(set symbol new-value)`
<a id="set"></a>
```
Modifies an existing variable
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
## `(macro name (params...) body...)`
<a id="macro"></a>
```
Defines a new macro
```
<br>
## `(eval statements...)`
<a id="eval"></a>
```
Evaluates all statements
```
<br>
## `(print args...)`
<a id="print"></a>
```
Outputs arguments
```
<br>
## `(pprint args...)`
<a id="pprint"></a>
```
Outputs values with pretty formatting
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
