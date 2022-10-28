phone=['one+','samsung','realme','apple','poco','vivo','oopo','redme','honor','nokia']
print(phone)
# ['one+','samsung','realme','apple','poco','vivo','oopo','redme','honor','nokia']

# list remove method works as remove the selective argument from the list
phone.remove('oopo')
print(phone)
# ['one+', 'samsung', 'realme', 'apple', 'poco', 'vivo', 'redme', 'honor', 'nokia']

phone.remove('one+')
print(phone)
# ['samsung', 'realme', 'apple', 'poco', 'vivo', 'redme', 'honor', 'nokia']
phone.remove('java')
print(phone)
#     phone.remove('java')
# ValueError: list.remove(x): x not in list