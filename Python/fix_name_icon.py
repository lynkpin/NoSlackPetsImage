import os
import sys

def batch_rename(start_num, target_dir=None):
    # 确定目标目录（默认使用脚本执行目录）
    if target_dir is None:
        target_dir = os.getcwd()  # 获取当前工作目录的完整路径
    
    # 遍历目录下的所有文件（获取完整路径）
    for file_name in os.listdir(target_dir):
        file_path = os.path.join(target_dir, file_name)  # 拼接完整文件路径
        
        # 只处理文件，跳过文件夹
        if not os.path.isfile(file_path):
            continue
        
        # 匹配目标文件格式：ornxxN_200.png 或 ornxxN_512.png
        if file_name.startswith('ornxx') and (file_name.endswith('_200.png') or file_name.endswith('_512.png')):
            try:
                # 提取原始序号（如ornxx10_200.png中的10）
                num_part = file_name.split('ornxx')[1].split('_')[0]
                original_num = int(num_part)
            except (IndexError, ValueError):
                print(f"跳过不符合格式的文件：{file_name}")
                continue
            
            # 计算新序号
            new_num = start_num + original_num - 1
            # 构建新文件名和新文件路径
            suffix = file_name.split('_')[1]  # 获取_200.png或_512.png
            new_file_name = f"orn{new_num}_{suffix}"
            new_file_path = os.path.join(target_dir, new_file_name)
            
            # 关键：重命名前先检查原文件是否存在
            if not os.path.exists(file_path):
                print(f"警告：原文件不存在，跳过 → {file_path}")
                continue
            
            # 执行重命名（使用完整路径）
            os.rename(file_path, new_file_path)
            print(f"已重命名：{file_name} → {new_file_name}")

if __name__ == "__main__":
    # 检查参数
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("用法1（文件在脚本目录）：python rename_script.py <起始数字>")
        print("用法2（指定文件目录）：python rename_script.py <起始数字> <文件目录路径>")
        print("示例1：python rename_script.py 373")
        print("示例2：python rename_script.py 373 D:\\images")
        sys.exit(1)
    
    # 解析参数
    try:
        start_num = int(sys.argv[1])
    except ValueError:
        print("错误：起始数字必须是整数（如373）")
        sys.exit(1)
    
    target_dir = sys.argv[2] if len(sys.argv) == 3 else None
    
    # 执行重命名
    batch_rename(start_num, target_dir)