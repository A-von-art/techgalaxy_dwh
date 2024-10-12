import json

# Преобразование products.json
with open('products.json', 'r', encoding='utf-8') as infile, open('products_ndjson.json', 'w', encoding='utf-8') as outfile:
    data = json.load(infile)
    for entry in data:
        json.dump(entry, outfile, ensure_ascii=False)
        outfile.write('\n')

# Преобразование orders.json
with open('orders.json', 'r', encoding='utf-8') as infile, open('orders_ndjson.json', 'w', encoding='utf-8') as outfile:
    data = json.load(infile)
    for entry in data:
        json.dump(entry, outfile, ensure_ascii=False)
        outfile.write('\n')
