import webbrowser
import os

html_file = "index.html"

url = f"file://{os.path.abspath(html_file)}"
webbrowser.open(url)