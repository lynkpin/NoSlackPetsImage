import os
import sys
import argparse
import re

def extract_number(filename):
    """从文件名中提取数字，用于排序"""
    # 使用正则表达式提取文件名中的数字
    numbers = re.findall(r'\d+', filename)
    if numbers:
        return int(numbers[0])
    return 0  # 如果没有数字，返回0放在最前面

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='批量重命名图片文件为orn+数字格式')
    parser.add_argument('directory', help='图片所在的目录路径')
    parser.add_argument('start_number', type=int, help='起始数字，例如101')
    args = parser.parse_args()

    # 检查目录是否存在
    if not os.path.isdir(args.directory):
        print(f"错误：目录 '{args.directory}' 不存在")
        sys.exit(1)

    # 定义支持的图片文件扩展名
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tga', '.psd', '.exr', '.hdr')
    
    # 获取目录中所有图片文件
    image_files = []
    for filename in os.listdir(args.directory):
        if filename.lower().endswith(image_extensions):
            image_files.append(filename)
    
    if not image_files:
        print(f"在目录 '{args.directory}' 中未找到任何图片文件")
        sys.exit(0)
    
    # 按文件名中的数字进行排序
    image_files.sort(key=lambda x: extract_number(x))
    
    # 重命名文件
    current_number = args.start_number
    renamed_count = 0
    
    for filename in image_files:
        # 获取文件扩展名
        ext = os.path.splitext(filename)[1].lower()
        
        # 构建新文件名
        new_filename = f"orn{current_number}{ext}"
        old_path = os.path.join(args.directory, filename)
        new_path = os.path.join(args.directory, new_filename)
        
        # 避免覆盖已存在的文件
        if os.path.exists(new_path):
            print(f"警告：文件 '{new_filename}' 已存在，跳过重命名 '{filename}'")
            continue
        
        # 执行重命名
        os.rename(old_path, new_path)
        print(f"重命名: {filename} -> {new_filename}")
        
        current_number += 1
        renamed_count += 1
    
    print(f"\n操作完成，成功重命名 {renamed_count} 个文件")

if __name__ == "__main__":
    main()
    