import os
import io
import shutil
import time
import requests

RULE_URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/"
RULE_URL1 = "https://raw.githubusercontent.com/RuCu6/QuanX/main/"
RULE_URL2 = "https://raw.githubusercontent.com/fmz200/wool_scripts/main/QuantumultX/"
RULE_URL3 = "https://raw.githubusercontent.com/GiveYou32Likes/"

RULES = {
    "CorrectionRule": {
        "Direct": RULE_URL + "Surge/Direct/Direct.list",
        "MyCorrectionRule": RULE_URL3 + "Profile/main/QuantumultX/Rule/CorrectionRule.list",
    },
    "RejectRule": {
        "MyBlockAds": RULE_URL1 + "Rules/MyBlockAds.list",
        "fenliu": RULE_URL2 + "filter/fenliu.list",
        "AdvertisingLite": RULE_URL + "Clash/AdvertisingLite/AdvertisingLite.list",
        "MyRejectRule": RULE_URL3 + "Profile/main/QuantumultX/Rule/RejectRule.list",
    },
    "ProxyRule": {
        "Proxy": RULE_URL + "Clash/Proxy/Proxy.list",
        "MyProxyRule": RULE_URL3 + "Profile/main/QuantumultX/Rule/ProxyRule.list",
    },
    "DirectRule": {
        "China": RULE_URL + "Clash/China/China.list",
        "ChinaASN": RULE_URL + "Surge/ChinaASN/ChinaASN.list",
        "Lan": RULE_URL + "Surge/Lan/Lan.list",
    },
    "USRule": {
        "OpenAI": RULE_URL + "Surge/OpenAI/OpenAI.list",
        "Claude": RULE_URL + "Surge/Claude/Claude.list",
        "PayPal": RULE_URL + "Surge/PayPal/PayPal.list",
    },
    "StreamingRule": {
        "Netflix": RULE_URL + "Surge/Netflix/Netflix.list",
        "Disney": RULE_URL + "Surge/Disney/Disney.list",
        "YouTube": RULE_URL + "Surge/YouTube/YouTube.list",
        "Spotify": RULE_URL + "Surge/Spotify/Spotify.list",
    }
}

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

def load_file(rules_dict, file_dir):
    target_directory = os.path.join("Surge", file_dir)

    # 使用os.makedirs来递归创建目录
    os.makedirs(target_directory, exist_ok=True)

    for key, url in rules_dict.items():
        response = requests.get(url, headers=HEADER)
        if response.status_code == 200:
            with open(os.path.join(target_directory, f"{key}.list"), "wb") as f:
                shutil.copyfileobj(io.BytesIO(response.content), f)
            time.sleep(1)
    print(f"下载 {file_dir} 文件成功")

def remove():
    for folder in RULES.keys():
        if os.path.exists(folder):
            shutil.rmtree(folder)
    print("删除旧文件成功")

if __name__ == '__main__':
    remove()
    for folder, rules in RULES.items():
        load_file(rules, folder)
