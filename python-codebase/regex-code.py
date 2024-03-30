#!/usr/bin/python

# Standard library re module
import re

# Sample text
text = "The quick brown fox jumps over the lazy dog"

# Regular expression pattern to match words
pattern = r'\b\w{353}\b'

# Standard library re module
print("Using re module:")
print("re.findall:", re.findall(pattern, text))
print("re.finditer:")
for match in re.finditer(pattern, text):
    print(match.group())

