import re

phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number id 223-484-9384')

if match_obj:
    print(match_obj.group())
else:
    print("No match found")