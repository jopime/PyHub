# Parsing XML data and converting it to JSON data or into Python dictionary.
# You can already read from a file and perform conversion.
# Or use requests to get data from the internet and convert data -> RSS feeds.

import xmltodict
import json

my_xml = """
    <user>
      <id hello="world">!</id>
      <name>Vijay</name>
      <github>SVijayB</github>
    </user>
"""

data_dict = xmltodict.parse(my_xml)
json_data = json.dumps(data_dict)
print(json_data)