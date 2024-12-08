import wikipediaapi
import string
import csv

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'ru')

page = wiki_wiki.page("Категория:Животные_по_алфавиту")
print(page.text)

def print_categorymembers(categorymembers, level=0, max_level=1):
    alpha_list = []
    for char in list(string.ascii_uppercase):
        alpha_char = {}
        counter = 0
        for c in categorymembers.values():
            if c.ns == 0 and c.title.startswith(char):
                counter += 1
        alpha_char['char'] = char
        alpha_char['count'] = counter
        alpha_list.append(alpha_char)
        print(alpha_list)
    return alpha_list


print("Category members: Категория:Животные_по_алфавиту")
# print_categorymembers(page.categorymembers, level=0, max_level=0)
result = print_categorymembers(page.categorymembers)
print(result)
with open("mycsvfile.csv", "w", newline="") as f:
    w = csv.DictWriter(f, ['char', 'count'])
    # w.writeheader()
    w.writerows(result)
