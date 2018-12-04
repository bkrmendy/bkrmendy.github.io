#!/usr/bin/env python3

import os
import sys

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {{
    background: #eff2d8;
    font-family: sans-serif;
}}
.title {{
    text-align: center;
}}
.accordion {{
    width: 80%;
    margin: 5px auto;
    background-color: #81b0b2;
    color: #444;
    cursor: pointer;
    padding: 18px;
    border: none;
    text-align: left;
    outline: none;
    font-size: 15px;
    font-weight: bold;
    transition: 0.4s;
    display: block;
}}
.active, .accordion:hover {{
    background-color: #00738c;
}}
.panel {{
    padding: 0 18px;
    width: 75%;
    margin: 5px auto;
    display: none;
    overflow: hidden;
}}
</style>
</head>
<body>

<h2 class="title">KÉRDÉSEK</h2>

{0}

<script>
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {{
    acc[i].addEventListener("click", function() {{
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {{
            panel.style.display = "none";
        }} else {{
            panel.style.display = "block";
        }}
    }});
}}
</script>

</body>
</html>"""

SECTION_TEMPLATE = """<button class="accordion">{0}</button>
<div class="panel">
  {1}
</div>
"""

def parse_section(section):
    lines = section.split('\n')
    return (lines[0][2:], '\n'.join(["<p>{0}</p>".format(i) for i in lines[1:]] ))

def parse_file(path):
    with open(path, 'r') as file:
        content = file.read().strip()
        content = filter(lambda a: a != '', content.split('\n\n'))
        return list(map(parse_section, content))

def parse_folder(path):
    files = [os.path.join(path, file) for file in os.listdir(path) if '.md' in file]
    sections = list()
    for items in list(map(parse_file, files)): # make this a listcomp
        for item in items:
            sections.append(item)
    return sections

def generate_files(out_path, items):
    with open(os.path.join(out_path, 'index.html'), 'w') as out_file:
        sections = map(lambda x: str(SECTION_TEMPLATE).format(x[0], x[1]), items)
        out_file.writelines(str(PAGE_TEMPLATE).format(''.join(sections)))

def main():
    if len(sys.argv) < 3:
        print("Usage: ./generate.py <folder/file> <path_to_output_folder>")
        return
    path = sys.argv[1]
    output = sys.argv[2]
    if path[-3:] == '.md':
        generate_files(output, parse_file(path))
    else:
        generate_files(output, parse_folder(path))

if __name__ == "__main__":
    main()