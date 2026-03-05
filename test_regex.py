import os
import glob
import re

directory = r"c:\Users\kaviraja\Desktop\Sasstech\templates"

about_dropdown_pattern = re.compile(
    r'\s*<li class="nav-submenu__item[^>]*>\s*<a class="nav-submenu__link[^>]*href="/about"[^>]*>\s*About Us\s*</a>\s*</li>\n?', re.IGNORECASE
)

contact_button_pattern = re.compile(
    r'([ \t]*)<li class="nav-menu__item">\s*<a class="nav-menu__link[^>]*href="/contact"[^>]*>Contact</a>\s*</li>', re.IGNORECASE
)

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html.twig'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'href="/about"' in content and 'href="/contact"' in content:
                # Remove about from dropdown
                new_content = about_dropdown_pattern.sub('', content)
                
                # Add about before contact
                def replace_func(match):
                    indent = match.group(1)
                    full = match.group(0)
                    about_li = f'{indent}<li class="nav-menu__item">\n{indent}    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"\n{indent}        href="/about">About Us</a>\n{indent}</li>\n'
                    return about_li + full

                new_content = contact_button_pattern.sub(replace_func, new_content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")
