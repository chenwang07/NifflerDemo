import markdown2

with open(r"C:\Code\NifflerDemo\README.md", 'r') as md_file:
    md_text = md_file.read()
    html_text = markdown2.markdown(md_text)

with open(r"C:\Code\NifflerDemo\index.html", 'w') as html_file:
    html_file.write(html_text)