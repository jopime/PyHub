import mistune

markdown_data  = """
# Markdown parser
## Random stylings to explore mistune library
Hello **world**!
I am *Vijay*...
`I am on GitHub at SVijayB!`
"""

markdown = mistune.Markdown()
print(markdown(markdown_data)) # HTML TAGS

renderer = mistune.Renderer(escape=True, hard_wrap=True, use_xhtml = True)
markdown = mistune.Markdown(renderer=renderer)
print(markdown(markdown_data)) # XHTML TAGS

# PARSING DATA FROM MARKDOWN FILES DIRECTLY
f = open("README.md", "r")
file_data = f.read()
print(markdown(file_data))