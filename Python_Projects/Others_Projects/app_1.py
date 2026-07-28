import requests
from bs4 import BeautifulSoup
import re

def extract_mp4_links(url):
    """
    استخراج لینک‌های فایل‌های MP4 از یک صفحه
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # جستجوی لینک‌های MP4
        mp4_links = []
        
        # روش 1: تگ‌های video و source
        for video in soup.find_all('video'):
            for source in video.find_all('source'):
                if source.get('src') and source['src'].endswith('.mp4'):
                    mp4_links.append(source['src'])
        
        # روش 2: لینک‌های معمولی با پسوند mp4
        for link in soup.find_all('a', href=True):
            if link['href'].endswith('.mp4'):
                mp4_links.append(link['href'])
        
        # روش 3: با استفاده از regex
        text = response.text
        mp4_pattern = r'https?://[^\s"\'<>]+\.mp4'
        mp4_links.extend(re.findall(mp4_pattern, text))
        
        return list(set(mp4_links))  # حذف تکراری‌ها
    
    except Exception as e:
        print(f"خطا: {e}")
        return []

# مثال
url = "https://example.com/videos"
mp4_files = extract_mp4_links(url)

for mp4 in mp4_files:
    print(mp4)