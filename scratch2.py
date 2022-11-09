import webbrowser
import time


country = "Italy"

html_content = f"<html> <head> </head> <h1> {country} <body> </body>  </html>"

with open("index.html", "w") as html_file:
    html_file.write(html_content)
    print("Created")


time.sleep(2)
webbrowser.open_new_tab("index.html")
