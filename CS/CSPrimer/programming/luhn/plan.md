# Luhn algorithm

Luhn's algorithm is a check digit formula used to validate a variety of identification numbers (e.g., credit card numbers).

1. Drop the last digit from the number (check digit)
2. From right to left, starting from last, double every second digit and sum it's resulting digits.
3. Sum all the resulting digits
4. Check digit = (10 - (s mod 10))

Example: 

I have a payload (no check digit) and I want to compute it's check digit -> 1789372997

1. Already done
2. Double every second digit AND sum resulting digits
7 x 2 = 14 -> 5
9
9 x 2 = 18 -> 9
etc...
3. Sum all digits
56
4. Calculate check digit
(10 - (56 mod 10)) = 4

Hence the final number is 17893729974

To validate the check if a number is valid you drop the check digit, recalculate it and then compare the resulting check digit with the existing one.

What am I going to do?

- Create a verify() function that takes in a number and checks if the number is valid
- Create a add_check_digit() function that takes in a payload and adds a check digit
- Add tests to make sure that both functions work correctly
