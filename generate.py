import pathlib

# generate CSS for each theme by replacing CTPTHEME

if __name__ == "__main__":
    for theme in ("latte", "frappe", "macchiato", "mocha"):
        with open("css/BASE.css", "r") as base:
            data = base.read()
            data = data.replace("CTPTHEME", theme)
            
            pathlib.Path("dist").mkdir(exist_ok=True)
            with open(f"dist/{theme}.css", "w") as out:
                out.write(data)
