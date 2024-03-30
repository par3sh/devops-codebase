
import re
# re.search(pattern,string)
result = re.search(r'quick', 'The quick brown fox quick')
print(result)

if result:
    print('Pattern found:', result.group())

#\b\w{3,5}\b
    
matches = re.findall(r'quick', 'The quick brown fox jumps over The lazy dog quick')
print('Matches found:', matches)

iterator = re.finditer(r'quick', 'The quick brown fox jumps over the lazy dog quick')
for match in iterator:
    print(match)
    print('Match found:', match.group())

parts = re.split(r'\s', 'The quick brown fox')
print('Split parts:', parts)

new_string = re.sub(r'\bfox\b', 'dog', 'The quick brown fox')
print('Modified string:', new_string)

thisis123amail123abc@gmail.com
^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$

\w[a-z,A-Z,0-9]