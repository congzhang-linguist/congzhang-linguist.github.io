import re


def to_bib(bib_index, author, year, title, conference, time, location):
    print(f"@conference{{{bib_index}-c,\n"
          f"    bibtex_show={{true}},\n"
          f"    abbr={{xxx}},\n"
          f"    html={{xxx}},\n"
          f"    pdf={{xxx}},\n"
          f"    author       = {{{author}}},\n"
          f"    title        = {{{title}}},\n"
          f"    booktitle    = {{{conference}}},\n"
          f"    year         = {{{year}}},\n"
          f"    category	 = {{oral}},\n"
          f"    month		 = {{{time}}},\n"
          f"    location	 = {{{location}}},\n"
          f"    abstract     = {{xxx}}\n"
          f"}}\n")


with open('C:/Users/ncz2/OneDrive - Newcastle University/Documents/Website/congzhang-linguist.github.io/_bibliography/talks.txt',
        'r') as f:
    items = f.read().split('\\\\')
    for i in range(len(items)):
        # print('-->', i, items[i])
        if i > 0:
            # print('-->', items[i])
            item_lines = items[i].split('\n')
            # print('-->', len(item_lines))
            year = ''.join(re.findall(r'years\{(\d+)\}', item_lines[1]))
            author = item_lines[2].strip()
            title = item_lines[3].strip()
            bib_index = ''.join(author.lower().split(",")[0]) + year + ''.join(title.lower().split(" ")[0])
            conference = ''.join(re.findall(r'\\textit\{(.*)\}', item_lines[4]))
            if len(item_lines) > 5:
                # print('-->', items[i])
                time = ''.join(re.findall(r'\%\,\ (.*)', item_lines[5].split('.')[0]))
                location = ''.join(item_lines[5].split('.')[1]).strip()
                # print('-->', i, location)
                # to_bib(bib_index, author, year, title, conference, time, location)
            else:
                time = "xxx"
                location = "xxx"
            # print('-->', i)
            to_bib(bib_index, author, year, title, conference, time, location)