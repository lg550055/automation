import email
import re

email_pattern = r'\S+@\S+\.\w+'
phone_pattern = r'\d{3}-?\)?\d{3}-?\d{4}'

with open('potential-contacts.txt') as f:
  text = f.read()

print(text[:500])
