import opencc
import jieba
import pandas as pd
from qhchina.analytics.collocations import find_collocates

file_name = "data/luotuoxiangzi.txt" 
print(f"正在处理文本 {file_name}...")

cc = opencc.OpenCC('t2s')
with open(file_name, 'r', encoding='utf-8') as f:
    text = f.read()
text_simplified = cc.convert(text)

sentences = [list(jieba.cut(s)) for s in text_simplified.split('。') if len(s.strip()) > 0]

target_role = "祥子"  

configs = [
    {"method": "window", "horizon": 5, "filename": "window5.csv"},
    {"method": "window", "horizon": 10, "filename": "window10.csv"},
    {"method": "sentence", "filename": "sentence.csv"}
]

for config in configs:
    print(f"正在跑 {config['filename']}...")
    
    if config["method"] == "window":
        result = find_collocates(
            sentences,
            target_words=target_role,
            method="window",
            horizon=config["horizon"],
            filters={"min_word_length": 2, "max_p": 0.05}
        )
    else:
        result = find_collocates(
            sentences,
            target_words=target_role,
            method="sentence",
            filters={"min_word_length": 2, "max_p": 0.05}
        )
        
    result.to_csv(f"output/{config['filename']}", index=False)
    result.to_html(f"output/{config['filename']}.html", index=False, encoding="utf-8")

print("全跑完啦！")