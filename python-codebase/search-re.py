import re
name_pattern = r'name="([^"]*)"'
path_pattern = r'path="([^"]*)"'
with open("manifest/default.xml",'r') as read_obj:
    for line in read_obj:
        if '<project' in line:
            match_name = re.search(name_pattern,line)
            match_path = re.match(path_pattern,line)
            if match_name:
                name_value = match_name.group(1)
                path_value = match_path.group(1)
                print(name_value+" : "+path_value)


'''
name=": This part of the pattern matches the literal characters "name=". It ensures that the attribute we're interested in starts with the characters "name=".([^"]*):
[^"]: This part of the pattern matches any character except ". The ^ inside the square brackets [] negates the character class, meaning it matches any character that is not ".
*: This quantifier means "zero or more occurrences" of the preceding character class. So [^"]* matches zero or more occurrences of any character except ".
": This part of the pattern matches the closing " of the attribute value.
Putting it all together, name="([^"]*)" matches the following:c
'''