import os
import re
import datetime
import pytz

types = "QuantumultX/"
file_paths = [types + rule for rule in ["CorrectionRule", "DirectRule", "ProxyRule", "RejectRule", "StreamingRule", "USRule"]]
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
                        line = re.sub(r'\s+', '', line)
                        line = re.sub(r',no-resolve', '', line)
                        line = re.sub(r',(?:Netflix|Disney|YouTube|Spotify)$', ',Streaming', line)
                        line = re.sub(r',(?:ChinaASN|China|Direct|Lan)$', ',direct', line)
                        line = re.sub(r',(?:AdvertisingLite|Privacy|Hijacking|REJECT|Reject)$', ',reject', line)
                        line = re.sub(r',Proxy', ',proxy', line)
                        line = re.sub(r',(?:OpenAI|Claude|PayPal)$', ',US', line)
                        line = re.sub(r'^(?:host|domain|DOMAIN)', 'HOST', line)
                        line = re.sub(r'-suffix', '-SUFFIX', line)
                        line = re.sub(r'-keyword', '-KEYWORD', line)
                        line = re.sub(r'^ip-cidr', 'IP-CIDR', line)
                        line = re.sub(r'^ip6-cidr', 'IP6-CIDR', line)
                        line = re.sub(r'^user-agent', 'USER-AGENT', line)
                        modified_lines.append(line)  # 将修改后的行添加到新的列表
                    
                    data_set.update(modified_lines)
        data_list = sorted(data_set)
        out_f.writelines(line + '\n' for line in data_list if line.strip())
    return output_file_path

if __name__ == '__main__':
    for path in file_paths:
        # 创建文件夹，如果文件夹不存在
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"创建目录 {path} 成功")
            
        # 合并文件并去重
        output_file_path = merge_and_deduplicate_files(path)

        print(f"{os.path.basename(output_file_path)} 文件创建成功")
