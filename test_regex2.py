import os
import glob
import re

directory = r"c:\Users\kaviraja\Desktop\Sasstech\templates"

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html.twig'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find </li> followed by spaces and <li
            new_content = re.sub(r'</li>[ \t]{5,}<li', r'</li>\n                                    <li', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed indent in {filepath}")
