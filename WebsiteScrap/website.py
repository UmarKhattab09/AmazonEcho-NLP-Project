from bs4 import BeautifulSoup
import requests
import os
import pathlib
import sys
import pandas as pd
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

class WebsiteScrapper:
  def __init__(self,url):
    self.url = url
  def websitename(self):
    parts = self.url.split('/')
    try:
        name_part = parts[3].replace('-', '')
        return name_part
    except IndexError:
        return "defaultname"
    


  def scraping(self,url):
    response = requests.get(url)
    name = self.websitename()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    div_with_data_hook = soup.find_all('div', attrs={'data-hook': 'review-collapsed'})
    data = []
    for div in div_with_data_hook:
      data.append(div.get_text())
    if data == []:
      return f"The Following Link is not scrappable"
    else:
      hasmap = {
          name:data
      }
      df = pd.DataFrame(hasmap)

      df.to_csv(f"outputs/{name}.csv")

      return df
    


# test1 = WebsiteScrapper("https://www.amazon.com/iPhone-Charger-Anker-AirPods-Included/dp/B0C8HHV9DK/?_encoding=UTF8&pd_rd_w=Zizz0&content-id=amzn1.sym.f2128ffe-3407-4a64-95b5-696504f68ca1&pf_rd_p=f2128ffe-3407-4a64-95b5-696504f68ca1&pf_rd_r=JTNG8GHDS8903AADTJ34&pd_rd_wg=PWDJB&pd_rd_r=a257b401-3d62-4bd7-a869-76767d49f2b0&ref_=pd_hp_d_btf_crs_zg_bs_541966&th=1")
test2 = WebsiteScrapper("https://www.amazon.com/Charger-charging-Certified-lightning-AirPods/dp/B0B283QP2N/?_encoding=UTF8&pd_rd_w=xI3Mi&content-id=amzn1.sym.117cb3e1-fd12-46a0-bb16-15cd49babfdb%3Aamzn1.symc.abfa8731-fff2-4177-9d31-bf48857c2263&pf_rd_p=117cb3e1-fd12-46a0-bb16-15cd49babfdb&pf_rd_r=1A0Y3SCKF61QZME5WKSB&pd_rd_wg=ZWwxr&pd_rd_r=ae81b6c3-d9bd-471e-908b-d82eca3bdbf3&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d")
# df1 = test1.scraping(test1.url)
df2 = test2.scraping(test2.url)


