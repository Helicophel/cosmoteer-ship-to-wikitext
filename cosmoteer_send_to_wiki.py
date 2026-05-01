from mwcleric import WikiggClient
from mwcleric.auth_credentials import AuthCredentials
import os
import time

#you need to create your own user and credentials files
credentials = AuthCredentials(user_file="me")
site = WikiggClient('cosmoteer', credentials=credentials)
summary = 'Ship File Upload'

for file in os.listdir("wikitext"):
    with open(f'wikitext/{file}', "r", encoding="utf-8") as f:
        title = file.replace(".txt", "")
        page = site.client.pages[title]
        if not page.exists:
            content = f.read()
            site.save(page, content, summary)
            print(f'uploaded page {title}')
            time.sleep(10)
        else:
            print(f"skipped page {title}")
    #to avoid rate limits, arbritary timing
    
