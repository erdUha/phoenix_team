import json
data = json.load(open('bruh.json', 'r'))

result = {}

i = 0
for value in data:
    if value not in result.values():
        result[i] = value
        i += 1

print(result)
