import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
new_list = []
for person in contacts_list:
    name = " ".join(person[: 3]).split(' ')[:3]
    search_phone = re.findall(r'\d+', person[5])
    full_phone = ''.join(search_phone)
    phone = re.sub(r'\+?(\d)(\d{3})(\d{3})(\d{2})(\d{2})', r'+7(\2)\3-\4-\5', full_phone[:11])
    add_phone = re.sub(r'(\d+)', r'доб.\1', full_phone[11:])
    if add_phone == '':
        person[5] = phone
    else:
        person[5] = ' '.join([phone, add_phone])
    new_person = name + person[3:]
    new_person_filtered = list(filter(lambda x: x[0] and x[1] in new_person, new_list))
    if new_person_filtered:
        new_list.remove(new_person_filtered[0])
        merge_person = zip(new_person, new_person_filtered[0])
        drop_duplicates = [list(set(x)) for x in list(merge_person)]
        drop_empty = list(map(lambda x: x.remove('') if '' in x and len(x) >= 2 else x, drop_duplicates))
        new_person = [x[0] for x in drop_duplicates]
    new_list.append(new_person)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)
