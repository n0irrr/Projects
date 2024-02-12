import pandas as pd
import requests
import gzip

req = requests.get('https://www.straitstimes.com/')
with gzip.open('req', 'rb') as f:
    file_content = f.read()

pd.set_option('max_colwidth', 1000)
pd.set_option('max_seq_item', 1000)
narutowiki = pd.read_html('https://naruto.fandom.com/wiki/Narutopedia')
