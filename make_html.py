import os

html = "<html><head><meta charset='utf-8'><title>搭配分析</title></head><body><h1>《骆驼祥子》角色搭配分析对比</h1>"

for title, f in [("窗口=5", "collocates_window5.csv.html"), ("窗口=10", "collocates_window10.csv.html"), ("句子共现", "collocates_sentence.csv.html")]:
    path = f"output/{f}"
    if os.path.exists(path):
        html += f"<h2>{title}</h2>"
        with open(path, "r", encoding="utf-8") as file:
            html += file.read()

html += "</body></html>"

with open("output/results.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("网页生成完毕！")

