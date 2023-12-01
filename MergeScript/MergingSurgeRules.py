import os
import re
import datetime
import pytz
import shutil
import time
import requests
from concurrent.futures import ThreadPoolExecutor

# 正则表达式替换规则
replacements = [
    (r'\s+', ''),
    (r',no-resolve', ''),
    (r',(?:DIRECT$|direct$|REJECT$|reject$|PROXY$|proxy$)', ''),
    (r'-suffix', '-SUFFIX'),
    (r'-keyword', '-KEYWORD'),
    (r'ip-cidr', 'IP-CIDR'),
    (r'^(?:host|HOST)', 'DOMAIN'),
    (r'IP6-CIDR', 'IP-CIDR6'),
]

RULES = {
    "CorrectionRule": {
        "fenliuxiuzheng": "https://raw.githubusercontent.com/fmz200/wool_scripts/main/QuantumultX/filter/fenliuxiuzheng.list",
        "MyCorrectionRule": "https://raw.githubusercontent.com/GiveYou32Likes/Profile/main/QuantumultX/Rule/CorrectionRule.list",
    },
    "RejectRule": {
        "fenliu": "https://raw.githubusercontent.com/fmz200/wool_scripts/main/QuantumultX/filter/fenliu.list",
        "Privacy": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Privacy/Privacy.list",
        "Hijacking": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Hijacking/Hijacking.list",
        "MyBlockAds": "https://raw.githubusercontent.com/RuCu6/QuanX/main/Rules/MyBlockAds.list",
        "MyRejectRule": "https://raw.githubusercontent.com/GiveYou32Likes/Profile/main/QuantumultX/Rule/RejectRule.list",
        "BlockHttpDNS": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/BlockHttpDNS/BlockHttpDNS.list",
    },
    "ProxyRule": {
        "Proxy": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Proxy/Proxy.list",
        "MyProxyRule": "https://raw.githubusercontent.com/GiveYou32Likes/Profile/main/QuantumultX/Rule/ProxyRule.list",
    },
    "DirectRule": {
        "Apple": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Apple/Apple.list",
        "Microsoft": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Microsoft/Microsoft.list",
        "Speedtest": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Speedtest/Speedtest.list",
        "China": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/China/China.list",
        "ChinaASN": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/ChinaASN/ChinaASN.list",
    },
    "USRule": {
        "OpenAI": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/OpenAI/OpenAI.list",
        "Claude": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Claude/Claude.list",
        "PayPal": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PayPal/PayPal.list",
        "Google": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Google/Google.list",
        "Bing": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Bing/Bing.list",
    },
    "StreamingRule": {
        "Netflix": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Netflix/Netflix.list",
        "Disney": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Disney/Disney.list",
        "YouTube": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/YouTube/YouTube.list",
        "Spotify": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Spotify/Spotify.list",
        "AppleTV": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AppleTV/AppleTV.list",
    }
}

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
TYPES = "Surge"
file_paths = [TYPES + "/" + rule for rule in RULES.keys()]

def download_and_save_file(url, target_path):
    response = requests.get(url, headers=HEADER)
    if response.status_code == 200:
        with open(target_path, "wb") as f:
            f.write(response.content)
        time.sleep(1)

def apply_replacements(line):
    for pattern, replacement in replacements:
        line = re.sub(pattern, replacement, line)
    return line

def load_files(rules, folder):
    target_directory = os.path.join(TYPES, folder)
    os.makedirs(target_directory, exist_ok=True)

    with ThreadPoolExecutor() as executor:
        futures = []
        for rule_name, rule_url in rules.items():
            target_path = os.path.join(target_directory, f"{rule_name}.list")
            futures.append(executor.submit(download_and_save_file, rule_url, target_path))
        
        for future in futures:
            future.result()
        print(f"新文件已下载至：{target_directory}")

def remove_old_files():
    for folder in RULES.keys():
        target_directory = os.path.join(TYPES, folder)
        if os.path.exists(target_directory):
            shutil.rmtree(target_directory)
            print(f"已删除旧文件夹：{target_directory}")
        else:
            print(f"旧文件夹不存在：{target_directory}")

def remove_old_files_except_merged(path):
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path) and file_name != f"{os.path.basename(path)}.list":
            os.remove(file_path)
            print(f"已删除文件：{file_path}")

def merge_and_deduplicate_files(path):
    output_file_path = os.path.join(path, f"{os.path.basename(path)}.list")
    with open(output_file_path, 'w', encoding='utf8') as out_f:
        # 插入当前时间行
        china_timezone = pytz.timezone('Asia/Shanghai')
        current_time = datetime.datetime.now(china_timezone).strftime("%Y-%m-%d %H:%M:%S")
        out_f.write(f"# 更新时间： {current_time}\n")
        data_set = set()  # 使用集合去重
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf8') as in_f:
                    lines = [line.strip() for line in in_f.readlines() if not (line.startswith("#") or line.startswith(";"))]
                    
                    # 使用正则表达式替换和过滤
                    modified_lines = []  # 创建新的列表来存储修改后的行
                    for i, line in enumerate(lines):
                        line = apply_replacements(line)  # 应用替换规则
                        modified_lines.append(line)  # 将修改后的行添加到新的列表
                    
                    data_set.update(modified_lines)
        data_list = sorted(data_set)
        data_list = [line for line in data_list if line.strip()]
        out_f.writelines(line + '\n' for line in data_list if line.strip())
    return output_file_path

if __name__ == '__main__':
    remove_old_files()  # 删除旧文件夹
    for folder, rules in RULES.items():
        load_files(rules, folder)
    for path in file_paths:
        # 创建文件夹，如果文件夹不存在
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"创建目录 {path} 成功")
            
        # 合并文件并去重
        output_file_path = merge_and_deduplicate_files(path)

        # 删除文件夹内的其他文件
        remove_old_files_except_merged(path)

        print(f"{os.path.basename(output_file_path)} 文件创建成功")
