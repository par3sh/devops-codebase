# Regex

## Regular Expressions for Text Processing:

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters: `.` (any character), `*` (zero or more), `+` (one or more), `?` (zero or one), `[]` (character class), `|` (OR), `^` (start of a line), `$` (end of a line), etc.
- Examples of regex usage: matching emails, phone numbers, or extracting data from text.
- `re` module functions include `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and replacement.



## Python re Module

The `re` module in Python provides support for working with regular expressions. Regular expressions (regex) are powerful tools for pattern matching and text manipulation. This README provides an overview of the main functions and methods available in the `re` module, along with examples.
***
## Functions

### `re.compile(pattern, flags=0)`
- Compile a regular expression pattern into a regex object.
- Parameters:
  - `pattern`: The regular expression pattern to compile.
  - `flags`: Optional flags that modify the behavior of the regex (e.g., case-insensitive matching).
- Returns:
  - A compiled regex object.

```python
import re

pattern = re.compile(r'fox', re.IGNORECASE)
```
***
### `re.search(pattern, string, flags=0)`

- Search for the first occurrence of a pattern in a string.
- Parameters:
- pattern: The regular expression pattern to search for.
- string: The input string to search within.
- flags: Optional flags for modifying the search behavior.
- Returns:
- A match object if a match is found, or None otherwise.
```python
import re
result = re.search(r'quick', 'The quick brown fox')
if result:
    print('Pattern found:', result.group())
```
***

### `re.match(pattern, string, flags=0)`
- Match a pattern at the beginning of a string.
- Parameters:
- pattern: The regular expression pattern to match.
- string: The input string to match against.
- flags: Optional flags for modifying the matching behavior.
- Returns:
- A match object if the pattern matches at the beginning of the string, or None otherwise.
```python
result = re.match(r'The', 'The quick brown fox')
if result:
    print('Pattern found at the beginning:', result.group())
```
***
### `re.findall(pattern, string, flags=0)`
- Find all occurrences of a pattern in a string.
- Parameters:
- pattern: The regular expression pattern to search for.
- string: The input string to search within.
- flags: Optional flags for modifying the search behavior.
- Returns:
- A list containing all non-overlapping matches as strings.
```python
matches = re.findall(r'\b\w{3,5}\b', 'The quick brown fox jumps over the lazy dog')
print('Matches found:', matches)
```
***
### `re.finditer(pattern, string, flags=0)`
- Find all occurrences of a pattern in a string, returning an iterator of match objects.
- Parameters:
- pattern: The regular expression pattern to search for.
- string: The input string to search within.
- flags: Optional flags for modifying the search behavior.
- Returns:
- An iterator yielding match objects for each match found.
```python
iterator = re.finditer(r'\b\w{3,5}\b', 'The quick brown fox jumps over the lazy dog')
for match in iterator:
    print('Match found:', match.group())
```
***
### `re.split(pattern, string, maxsplit=0, flags=0)`
- Split a string by occurrences of a pattern.
- Parameters:
- pattern: The regular expression pattern to use as the delimiter.
- string: The input string to split.
- maxsplit: Optional maximum number of splits to perform.
- flags: Optional flags for modifying the splitting behavior.
- Returns:
- A list of substrings resulting from the split.
```python
parts = re.split(r'\s', 'The quick brown fox')
print('Split parts:', parts)
```
***
### `re.sub(pattern, repl, string, count=0, flags=0)`
- Replace occurrences of a pattern in a string with another string.
- Parameters:
- pattern: The regular expression pattern to search for.
- repl: The string to replace occurrences of the pattern.
- string: The input string to perform replacements on.
- count: Optional maximum number of replacements to perform.
- flags: Optional flags for modifying the substitution behavior.
- Returns:
- The modified string with replacements.
```python
new_string = re.sub(r'\bfox\b', 'dog', 'The quick brown fox')
print('Modified string:', new_string)
```
---
## Flags
- In the re module of Python, flags are optional parameters that modify the behavior of the regular expression pattern matching functions. Flags are represented as integers and are used to control aspects such as case sensitivity, multiline matching, and more

### `re.IGNORECASE`
```python
import re

# Example: Case-insensitive search
result = re.search(r'apple', 'An Apple a day keeps the doctor away', flags=re.IGNORECASE)
if result:
    print('Pattern found:', result.group())
```
### `re.MULTILINE`: This flag enables multiline matching, allowing `^` and `$` to match the start and end of each line within the input string.

```python
import re

# Example: Multiline matching
pattern = re.compile(r'^start.*end$', flags=re.MULTILINE)
text = '''start
this is a multiline
text with start and end
end'''

matches = pattern.findall(text)
print('Matches found:', matches)
```
---

## *References:*
* [Android Source-Code Manifest](https://android.googlesource.com/platform/manifest/) 
```shell
git clone https://android.googlesource.com/platform/manifest 
cd mnaifest
git checkout android-14.0.0_r29
```