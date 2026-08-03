import pyperclip
import re

text = pyperclip.paste()

num_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
num = num_pattern.search(text)
num = num.group() if num else None

email_pattern = re.compile(r'[\w.+-]+@gmail\.com')
email = email_pattern.search(text).group()
email = email.group() if email else None

result = '\n'.join(filter(None,[num, email]))

if result:
    pyperclip.copy(result)
    print(result)
else:
    print("Number and emails not found")