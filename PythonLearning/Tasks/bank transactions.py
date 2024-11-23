file_name = input()
with open(file_name, 'r') as f:
    new_bank_accounts = f.read().splitlines()
bank_accounts = []
for i in new_bank_accounts:
    bank_accounts.append(i.split(';'))
bank_accounts_dict = {}
for i in bank_accounts:
    update_item = {i[0]: 0}
    bank_accounts_dict.update(update_item)
for i in bank_accounts:
    update_item = {i[1]: 0}
    bank_accounts_dict.update(update_item)
for operation in bank_accounts:
    bank_accounts_dict[operation[0]] -= int(operation[2])
    bank_accounts_dict[operation[1]] += int(operation[2])
values = []
for k, v in bank_accounts_dict.items():
    if k == '000':
        continue
    values.append([k, v])
values.sort(key=lambda x: x[1])
print_vaules = []
for i in values:
    print_vaules.append(f'{i[0]} {i[1]}')
print(';'.join(print_vaules))
