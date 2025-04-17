import pathlib

# generate CSS for each theme by replacing CTPTHEME

BACKGROUNDS = {
    "latte": "https://ssl-forum-files.fobby.net/forum_attachments/0050/2033/lattebg.png",
    "frappe": "https://ssl-forum-files.fobby.net/forum_attachments/0050/2030/frappebg.png",
    "macchiato": "https://ssl-forum-files.fobby.net/forum_attachments/0050/2036/macchiatobg.png",
    "mocha": "https://ssl-forum-files.fobby.net/forum_attachments/0050/2039/mochabg.png"
}

if __name__ == "__main__":
    for theme in ("latte", "frappe", "macchiato", "mocha"):
        with open("css/BASE.css", "r") as base:
            data = base.read()
            data = data.replace("CTPTHEME", theme)
            data = data.replace("THEMEBACKGROUND", BACKGROUNDS[theme])
            
            pathlib.Path("dist").mkdir(exist_ok=True)
            with open(f"dist/{theme}.css", "w") as out:
                out.write(data)
