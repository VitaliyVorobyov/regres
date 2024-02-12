import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
new_list = []
for i in contacts_list:
    name = " ".join(i[: 3]).split(' ')[:3]
    search_phone = re.findall(r'\d+', i[5])
    if len(search_phone) > 0:
        full_phone = ''.join(search_phone)
        phone = re.sub(
            r'\+?(\d{1})\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})?[-\s]?(\d{2})?',
            r'+7(\2)\3-\4-\5', full_phone[:11])
        add_phone = re.sub(r'\s?\(?(\w{3}\.?)?\s?(\d+)\)?', r'доб.\1\2', full_phone[11:])
        i[5] = ' '.join([phone, add_phone])
        new_list.append(name + i[3:])
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)
