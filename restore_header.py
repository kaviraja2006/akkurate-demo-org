import os
import re
import urllib.request

bak_file = r'c:\Users\kaviraja\Desktop\Sasstech\templates\service-details.html.twig.bak'
target_file = r'c:\Users\kaviraja\Desktop\Sasstech\templates\service-details.html.twig'
image_dest = r'c:\Users\kaviraja\Desktop\Sasstech\public\images\thumbs\office-stock.jpg'
image_url = 'https://cdn.pixabay.com/photo/2016/10/11/21/43/office-1730939_1280.jpg' # alternative direct link just in case
original_url = 'https://pixabay.com/images/download/markusspiske-office-1730939_1920.jpg'

try:
    req = urllib.request.Request(original_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as response, open(image_dest, 'wb') as out_file:
        out_file.write(response.read())
except Exception as e:
    print(f"Failed to download image from primary URL: {e}")
    try:
        req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(image_dest, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e2:
        print(f"Failed to download from secondary URL: {e2}")
        fallback_url = 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1920'
        req = urllib.request.Request(fallback_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(image_dest, 'wb') as out_file:
            out_file.write(response.read())

with open(bak_file, 'r', encoding='utf-8') as f:
    bak_content = f.read()

header_match = re.search(r'(        <!-- ==================== Header Two Start Here ==================== -->.*?        <!-- ==================== Header Two End Here ==================== -->)', bak_content, re.DOTALL)
if header_match:
    original_header = header_match.group(1)
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = re.sub(r'        <!-- ==================== Header Start Here ==================== -->.*?        <!-- ==================== Header End Here ==================== -->', original_header, content, flags=re.DOTALL)
    
    content = content.replace("url('https://pixabay.com/images/download/markusspiske-office-1730939_1920.jpg')", "url('/images/thumbs/office-stock.jpg')")
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success")
else:
    print("Header not found in backup")
