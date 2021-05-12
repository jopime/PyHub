import yaml

YAML_DATA = """
tools:
  - Git
  - GitHub
  - Vim
  - Linux
  - VSCode
languages:
  - Python
  - Java
  - C#
  - C++
"""

data = yaml.load(YAML_DATA, Loader=yaml.FullLoader)
print(data)

account_details = [{'account': 'GitHub', 'username': 'SVijayB'},
                   {'account': 'LinkedIn', 'username': 'SVijayB'}]
YAML_DATA = yaml.dump(account_details)
print(YAML_DATA)

with open('YAML_DATA.yaml', 'w') as f:
    data = yaml.dump(account_details, f)