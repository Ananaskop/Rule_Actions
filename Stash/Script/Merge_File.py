import os
import re
import datetime
import pytz

TYPES = "Stash"
file_paths = [TYPES + "/" + rule for rule in ["CorrectionRule", "DirectRule", "ProxyRule", "RejectRule", "StreamingRule", "USRule"]]
payload = "payload:"
def merge_and_deduplicate_files(path):

    output_file_path = os.path.join(path, f"{os.path.basename(path)}.yaml")
    with open(output_file_path, 'w', encoding='utf8') as out_f:
        # 插入当前时间行
        china_timezone = pytz.timezone('Asia/Shanghai')
        current_time = datetime.datetime.now(china_timezone).strftime("%Y-%m-%d %H:%M:%S")
        out_f.write(f"# 更新时间： {current_time}\n")
        # 插入 payload 行
        out_f.write(payload + '\n')
        data_set = set()  # 使用集合去重
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf8') as in_f:
                    lines = [line.strip() for line in in_f.readlines() if not (line.startswith("#") or line.startswith(";")or line.startswith("USER-AGENT"))]

                    # 使用正则表达式替换和过滤
                    for i, line in enumerate(lines):
                        line = re.sub(r'\s+', '', line)
                        line = re.sub(r',no-resolve', '', line)
                        line = re.sub(r',(?:DIRECT$|direct$|REJECT$|reject$|PROXY$|proxy$)', '', line)
                        line = re.sub(r'-suffix', '-SUFFIX', line)
                        line = re.sub(r'-keyword', '-KEYWORD', line)
                        line = re.sub(r'ip-cidr', 'IP-CIDR', line)
                        line = re.sub(r'^(?:host|HOST)', 'DOMAIN', line)
                        line = re.sub(r'IP6-CIDR', 'IP-CIDR6', line)               
                        lines[i] = line

                    data_set.update(lines)
        data_list = sorted(data_set)
        # 在每行前面增加 "-"
        data_list = [line for line in data_list if line.strip()] 
        data_list = ['  - ' + line for line in data_list]
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