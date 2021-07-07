#A veces tenemos un objeto tan complicado de construir que necesitamos varios builders para construirlo

text = "hello"
parts = ["<p>", text, "</p>"]

words = ["hello", "world"]
parts = ["<ul>"]
for w in words:
    parts.append(f" <li>{w}</li>")
parts.append("</ul>")
print("\n".join(parts))