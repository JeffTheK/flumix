---
title: Object Oriented Programming
description: Object oriented programming functions and variables
---

# Object Oriented Programming

### class

```lisp
(class name (instance-variables...))
```

Defines a new class. Creates a constructor `name/new` where `name` is your class name

### getp

```lisp
(getp property instance)
```

Returns property from class instance

### setp

```lisp
(setp property instance value)
```

Modifies a property from class instance