import re

text = "The quick brown fox jumps over the lazy dog."

# Find all occurrences of a pattern
matches = re.findall("the",text,re.IGNORECASE)
print(f"The Matches are:{matches}")

# Replace all occurrences of a pattern

replace = re.sub("fox","Dog",text)
print(f"New Text:{replace}")

replace1 = re.sub("dog","FOX",text)
print(f"New Text:{replace1}")