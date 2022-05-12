import email
import re

email_pattern = r'\S+@\S+\.\w+'
phone_pattern = r'\d{3}-?\)?\d{3}-?\d{4}'

with open('potential-contacts.txt') as f:
  text = f.read()

# Find all emails, order and write them to emails.txt
emails = re.findall(email_pattern, text)
emails.sort()
with open('emails.txt', 'w') as f:
  for e in emails:
    f.write(e+'\n')

# Find all phone numbers, order and write them to phone_numbers.txt
phones = re.findall(phone_pattern, text)
phones.sort()
with open('phone_numbers.txt', 'w') as f:
  for p in phones:
    f.write(p+'\n')

print ('Emails found' +len(emails))
print ('Phones found' +len(phones))
