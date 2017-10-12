import requests
from bs4 import BeautifulSoup


item = str(input("Item name:"))  # asks for item name
item2 = item.replace(" ", "_")  # replaces the spaces with underscores so we can use it in the url

r = requests.get("http://oldschoolrunescape.wikia.com/wiki/Exchange:"+item2)
soup = BeautifulSoup(r.text, 'html.parser')
# requests the page and parses it to read

for id in soup.findAll('span'):
    if id.has_attr("id"):
        if id['id'] == 'GEDBID':
            item_number = str(id.string)
# finds and saves the ID number of item


z = requests.get("http://services.runescape.com/m=itemdb_oldschool/Runescape/viewitem?obj="+str(item_number))
soup = BeautifulSoup(z.text, 'html.parser')
# requests ge price page with the item ID saved from before

results = soup.find_all(['h3'])
# finds all the h3 tags within the page

records = []
for result in results:
  url = result.find('span')
  records.append(url)
# finds the span tag with the h3 tag, this one is used for the price

print (item + ":", result.text)
# prints the item name specified earlier and the current guide price
