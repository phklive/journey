# Lecture 03 - Higher order procedures

## Summary

## Questions

## Lecture

We want to brake this brick wall that we have in our minds separating DATA (stuff) and ACTIONS (functions / manipulations on DATA).

In functional programming languages we can have `functions as data` a concept where we can pass a function as an argument to another function, Ex:

In this example we will create a function `sum` that takes 3 arguments as input:

- FN: another function
- a: a number
- b: a number

This function will sum the results of applying the function FN to `a` a certain number of times until a > b. This function uses recursion.

```scheme
(define (sum FN a b)
    (if (> a b)
        0
        (+ (FN a) (sum FN (+ a 1) b))))

(define (square x) (* x x))

(define (cube x) (* x x x))

(sum square 3 5) # answer will be 50

(sum cube 3 5) # answer will be 216
```

In this example we pass the function `square` as DATA, as an argument of the function `sum` we could have created a function `cube` and passed it as argument too, we hence understand that the `sum` function is agnostic over the passed in arguments.

Evaluating is not the same thing as invocing it. This is why Scheme is not throwing an error when we pass a function as an argument because it's only evaluating it an not invocing it.

Definitions:

- Domain of a function: what the function takes as input (arguments)
- Range of a function: what the function outputs (returns)
