import pyperclip
import re

text = pyperclip.paste()
num_pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

num = num_pattern.search(text)
num = num.group() if num else None

email_pattern = re.compile(r'''(
                [a-zA-Z0-9._%+-]+  # Username
                @  # @ symbol
                [a-zA-Z0-9.-]+  # Domain name
                (\.[a-zA-Z]{2,4})  # Dot-something
                )''', re.VERBOSE)      #re.compile(r'[\w.+-]+@gmail\.com')
email = email_pattern.search(text)
email = email.group() if email else None

result = '\n'.join(filter(None,[num, email]))

if result:
    pyperclip.copy(result)
    print(result)
else:
    print("Number and emails not found")