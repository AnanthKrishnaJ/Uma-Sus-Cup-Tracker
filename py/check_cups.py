import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = {')
end = html.find('};', start) + 1
data_str = html[start+21:end]

# It might not be perfectly valid JSON because of unquoted keys or comments.
# Let's just find the races array using string manipulation and regex, or write a custom parser.
import re

# Find Sus Cup 22
sc22_idx = data_str.find('Sus Cup 22')
print("Found Sus Cup 22 context:", data_str[sc22_idx-100:sc22_idx+500])

sc23_idx = data_str.find('Sus Cup 23')
print("Found Sus Cup 23 context:", data_str[sc23_idx-100:sc23_idx+500])

sc24_idx = data_str.find('Sus Cup 24')
print("Found Sus Cup 24 context:", data_str[sc24_idx-100:sc24_idx+500])

