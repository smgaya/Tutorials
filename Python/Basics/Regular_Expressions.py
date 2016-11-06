"""
Identifiers:

\d (any number)
\D (anything but a number)
\s (space)
\S (anything but a space)
\w (any character)
\W (anything but a character)
.  (any character, except for a new line)
\b (whitespace around words)
\. (period)

Modifiers:

{1, 3} (we're expecting 1-3)
+ (match 1 or more)
? (match 0 or 1)
* (match 0 or more)
$ (match end of a string)
^ (match start of a string)
| (either or)
[] (range or "variance")
{x} (expecting "x" amount)

White Space Characters:

\n (new line_
\s (space)
\t (tab)
\e (escape)
\f (form feed)
\r (return)

DONT FORGET!
. + * ? [ ] $ ^ { } ( ) | \
"""

import re

string = """
Jessice is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar is 102.
"""

ages = re.findall(r"\d{1,3}", string)
names = re.findall(r"[A-Z][a-z]*", string)

dict = {}
x = 0
for name in names:
    dict[name] = ages[x]
    x += 1

print(dict)
