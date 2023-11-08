import os
import io
import shutil
import time
import requests

RULES = {
    "CorrectionRule": {
        "Direct": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Direct/Direct.list",
        "MyCorrectionRule": "https://raw.githubusercontent.com/GiveYou32Likes/Profile/main/QuantumultX/Rule/CorrectionRule.list",
    },
    "RejectRule": {
        "Privacy": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Privacy/Privacy.list",
        "Hijacking": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Hijacking/Hijacking.list",
        "MyBlockAds": "https://raw.githubusercontent.com/RuCu6/QuanX/main/Rules/MyBlockAds.list",
        "fenliu": "https://raw.githubusercontent.com/fmz200/wool_scripts/main/QuantumultX/filter/fenliu.list",
        "MyRejectRule": "https://raw.githubusercontent.com/GiveYou32Likes/Profile/main/QuantumultX/Rule/RejectRule.list",
    },
    "ProxyRule": {
        "Proxy": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Proxy/Proxy.list",
        "MyProxyRule": "https://raw.githubusercontent.com/GiveYou32Likes/Profile/main/QuantumultX/Rule/ProxyRule.list",
    },
    "DirectRule": {
        "China": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/China/China.list",
        "Lan": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Lan/Lan.list",
    },
    "USRule": {
        "OpenAI": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.list",
        "Claude": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Claude/Claude.list",
        "PayPal": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PayPal/PayPal.list",
    },
    "StreamingRule": {
        "Netflix": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Netflix/Netflix.list",
        "Disney": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Disney/Disney.list",
        "YouTube": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.list",
        "Spotify": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Spotify/Spotify.list",
    }
}

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
TYPES = "Stash"

def load_file(rules_dict, file_dir):
    target_directory = os.path.join(TYPES, file_dir)

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
        target_directory = os.path.join(TYPES, folder)
        if os.path.exists(target_directory):
            shutil.rmtree(target_directory)
            print(f"已删除旧文件夹：{target_directory}")
        else:
            print(f"旧文件夹不存在：{target_directory}")

if __name__ == '__main__':
    remove()
    for folder, rules in RULES.items():
        load_file(rules, folder)
