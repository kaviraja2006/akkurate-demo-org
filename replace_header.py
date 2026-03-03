import re

filepath = r"c:\Users\kaviraja\Desktop\Sasstech\templates\service-details.html.twig"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_header = """        <!-- ==================== Header Start Here ==================== -->
        <header class="header py-0 position-absolute w-100 top-0 tw-start-0 tw-z-99 border-bottom border-white border-opacity-10">
            <div class="container">
                <nav class="d-flex align-items-center justify-content-between py-3">
                    <!-- Logo Start -->
                    <div class="logo d-flex align-items-center tw-gap-3">
                        <span class="tw-w-10 tw-h-10 bg-main-600 text-white rounded-circle d-flex justify-content-center align-items-center tw-text-xl group-hover">
                            <i class="ph-bold ph-waveform"></i>
                        </span>
                        <a class="link hover--translate-y-1 active--translate-y-scale-9" href="/">
                            <h4 class="tw-mb-0 text-white fw-bold">Akkurate</h4>
                        </a>
                    </div>
                    <!-- Logo End  -->
                    <!-- Menu Start  -->
                    <div class="header-menu d-lg-block d-none">
                        <ul class="nav-menu d-lg-flex align-items-center tw-gap-8">
                            <li class="nav-menu__item has-submenu">
                                <a class="nav-menu__link hover-text-main-600 tw-duration-200 text-white tw-py-4 fw-medium w-100 d-flex align-items-center tw-gap-1" href="javascript:void(0)">
                                    Demos <i class="ph-bold ph-caret-down tw-text-xs"></i>
                                </a>
                            </li>
                            <li class="nav-menu__item has-submenu">
                                <a class="nav-menu__link hover-text-main-600 tw-duration-200 text-white tw-py-4 fw-medium w-100 d-flex align-items-center tw-gap-1" href="javascript:void(0)">
                                    Pages <i class="ph-bold ph-caret-down tw-text-xs"></i>
                                </a>
                            </li>
                            <li class="nav-menu__item has-submenu">
                                <a class="nav-menu__link hover-text-main-600 tw-duration-200 text-white tw-py-4 fw-medium w-100 d-flex align-items-center tw-gap-1" href="javascript:void(0)">
                                    Portfolio <i class="ph-bold ph-caret-down tw-text-xs"></i>
                                </a>
                            </li>
                            <li class="nav-menu__item">
                                <a class="nav-menu__link hover-text-main-600 tw-duration-200 text-white tw-py-4 fw-medium w-100" href="/contact">Contact us</a>
                            </li>
                            <li class="nav-menu__item">
                                <a class="nav-menu__link hover-text-main-600 tw-duration-200 text-white tw-py-4 fw-medium w-100" href="javascript:void(0)">Docs</a>
                            </li>
                        </ul>
                    </div>
                    <!-- Menu End  -->
                    <!-- Header Right start -->
                    <div class="d-flex align-items-center tw-gap-6">
                        <a class="text-white hover-text-main-600 tw-text-xl tw-transition d-flex align-items-center justify-content-center bg-transparent border-0" href="javascript:void(0)">
                            <i class="ph-bold ph-circle-half-tilt"></i>
                        </a>
                        <a class="btn bg-white text-heading hover-bg-main-600 hover-text-white d-none d-sm-inline-flex align-items-center justify-content-center tw-gap-2 tw-px-6 tw-py-2 fw-semibold tw-rounded-md tw-transition group" href="/register">
                            <i class="ph-bold ph-user-circle group-hover-text-white text-heading tw-text-lg"></i> Sign up
                        </a>
                        <button class="toggle-mobileMenu leading-none d-lg-none text-white tw-text-9 bg-transparent border-0" type="button">
                            <i class="ph ph-list"></i>
                        </button>
                    </div>
                    <!-- Header Right End  -->
                </nav>
            </div>
        </header>
        <!-- ==================== Header End Here ==================== -->"""

pattern = r"        <!-- ==================== Header Two Start Here ==================== -->.*?        <!-- ==================== Header Two End Here ==================== -->"

new_content = re.sub(pattern, new_header, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated successfully!")
