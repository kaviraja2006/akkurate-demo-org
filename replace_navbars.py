import os
import re

directory = r"c:\Users\kaviraja\Desktop\Sasstech\templates"

# The new items to insert inside the main <ul class="nav-menu ...">
new_nav_items = """                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-heading tw-py-9 fw-semibold w-100"
                                        href="/">Home</a>
                                </li>
                                <li class="nav-menu__item has-submenu position-relative">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-heading tw-py-9 fw-semibold w-100"
                                        href="javascript:void(0)">Services</a>
                                    <ul
                                        class="nav-submenu scroll-sm position-absolute tw-start-0 top-100 tw-w-max bg-white tw-rounded-md overflow-y-auto tw-p-2 tw-mt-4 tw-duration-200 tw-z-99">
                                        <li class="nav-submenu__item d-block tw-rounded tw-duration-200 position-relative">
                                            <a class="nav-submenu__link hover-bg-neutral-200 text-heading fw-semibold w-100 d-block tw-py-2 tw-px-305 tw-rounded"
                                                href="/service-details">
                                                Service Details
                                            </a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-menu__item has-submenu position-relative">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-heading tw-py-9 fw-semibold w-100"
                                        href="javascript:void(0)">Industries</a>
                                    <ul
                                        class="nav-submenu scroll-sm position-absolute tw-start-0 top-100 tw-w-max bg-white tw-rounded-md overflow-y-auto tw-p-2 tw-mt-4 tw-duration-200 tw-z-99">
                                        <li class="nav-submenu__item d-block tw-rounded tw-duration-200 position-relative">
                                            <a class="nav-submenu__link hover-bg-neutral-200 text-heading fw-semibold w-100 d-block tw-py-2 tw-px-305 tw-rounded"
                                                href="#">
                                                Industry Details
                                            </a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"
                                        href="/project-details">Our Work</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"
                                        href="/blog">Blog</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"
                                        href="/about">About Us</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"
                                        href="/contact">Contact Us</a>
                                </li>
"""

# Same pattern but with white text color (e.g. for service-details header)
new_nav_items_white = """                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-white tw-py-9 fw-semibold w-100"
                                        href="/">Home</a>
                                </li>
                                <li class="nav-menu__item has-submenu position-relative">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-white tw-py-9 fw-semibold w-100"
                                        href="javascript:void(0)">Services</a>
                                    <ul
                                        class="nav-submenu scroll-sm position-absolute tw-start-0 top-100 tw-w-max bg-white tw-rounded-md overflow-y-auto tw-p-2 tw-mt-4 tw-duration-200 tw-z-99">
                                        <li class="nav-submenu__item d-block tw-rounded tw-duration-200 position-relative">
                                            <a class="nav-submenu__link hover-bg-neutral-200 text-heading fw-semibold w-100 d-block tw-py-2 tw-px-305 tw-rounded"
                                                href="/service-details">
                                                Service Details
                                            </a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-menu__item has-submenu position-relative">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-white tw-py-9 fw-semibold w-100"
                                        href="javascript:void(0)">Industries</a>
                                    <ul
                                        class="nav-submenu scroll-sm position-absolute tw-start-0 top-100 tw-w-max bg-white tw-rounded-md overflow-y-auto tw-p-2 tw-mt-4 tw-duration-200 tw-z-99">
                                        <li class="nav-submenu__item d-block tw-rounded tw-duration-200 position-relative">
                                            <a class="nav-submenu__link hover-bg-neutral-200 text-heading fw-semibold w-100 d-block tw-py-2 tw-px-305 tw-rounded"
                                                href="#">
                                                Industry Details
                                            </a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-white tw-py-9 fw-semibold w-100"
                                        href="/project-details">Our Work</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-white tw-py-9 fw-semibold w-100"
                                        href="/blog">Blog</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-white tw-py-9 fw-semibold w-100"
                                        href="/about">About Us</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-white tw-py-9 fw-semibold w-100"
                                        href="/contact">Contact Us</a>
                                </li>
"""

# Same pattern for mobile menu
new_nav_items_mobile = """                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-heading tw-py-9 fw-semibold w-100"
                                        href="/">Home</a>
                                </li>
                                <li class="nav-menu__item has-submenu position-relative">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-heading tw-py-9 fw-semibold w-100"
                                        href="javascript:void(0)">Services</a>
                                    <ul
                                        class="nav-submenu scroll-sm position-absolute tw-start-0 top-100 tw-w-max bg-white tw-rounded-md overflow-y-auto tw-p-2 tw-mt-4 tw-duration-200 tw-z-99">
                                        <li class="nav-submenu__item d-block tw-rounded tw-duration-200 position-relative">
                                            <a class="nav-submenu__link hover-bg-neutral-200 text-heading fw-semibold w-100 d-block tw-py-2 tw-px-305 tw-rounded"
                                                href="/service-details">
                                                Service Details
                                            </a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-menu__item has-submenu position-relative">
                                    <a class="nav-menu__link hover--translate-y-1 tw-pe-5 text-heading tw-py-9 fw-semibold w-100"
                                        href="javascript:void(0)">Industries</a>
                                    <ul
                                        class="nav-submenu scroll-sm position-absolute tw-start-0 top-100 tw-w-max bg-white tw-rounded-md overflow-y-auto tw-p-2 tw-mt-4 tw-duration-200 tw-z-99">
                                        <li class="nav-submenu__item d-block tw-rounded tw-duration-200 position-relative">
                                            <a class="nav-submenu__link hover-bg-neutral-200 text-heading fw-semibold w-100 d-block tw-py-2 tw-px-305 tw-rounded"
                                                href="#">
                                                Industry Details
                                            </a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"
                                        href="/project-details">Our Work</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"
                                        href="/blog">Blog</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"
                                        href="/about">About Us</a>
                                </li>
                                <li class="nav-menu__item">
                                    <a class="nav-menu__link hover--translate-y-1 text-heading tw-py-9 fw-semibold w-100"
                                        href="/contact">Contact Us</a>
                                </li>
"""

ul_pattern = re.compile(r'(<ul[^>]*class="[^"]*nav-menu(?!__)[^"]*"[^>]*>)')

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    offset = 0

    while True:
        match = ul_pattern.search(new_content, offset)
        if not match:
            break

        start_idx = match.end()
        ul_count = 1
        curr_idx = start_idx

        # find matching closing tag
        while ul_count > 0:
            next_open = new_content.find('<ul', curr_idx)
            next_close = new_content.find('</ul>', curr_idx)

            if next_close == -1:
                break # Malformed HTML

            if next_open != -1 and next_open < next_close:
                ul_count += 1
                curr_idx = next_open + 3
            else:
                ul_count -= 1
                curr_idx = next_close + 5
                
        if ul_count == 0:
            end_idx = curr_idx - 5
            
            # Determine which template it is
            is_white = 'text-white' in match.group(0) or 'home-two-header' in new_content[:start_idx] or '<!-- Nav menu Three Start -->' in new_content[start_idx-100:start_idx] or 'text-white' in new_content[start_idx:start_idx+100]
            
            # mobile menu usually has nav-menu--mobile
            is_mobile = 'nav-menu--mobile' in match.group(0)
            
            if is_mobile:
                replacement = "\n" + new_nav_items_mobile + "            "
            elif is_white:
                replacement = "\n" + new_nav_items_white + "                            "
            else:
                replacement = "\n" + new_nav_items + "                            "
                
            new_content = new_content[:start_idx] + replacement + new_content[end_idx:]
            offset = match.start() + len(replacement) + len(match.group(0))
        else:
            offset = start_idx

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")


for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html.twig'):
            filepath = os.path.join(root, file)
            process_file(filepath)
