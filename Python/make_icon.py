import os
from PIL import Image

def process_images(input_folder, output_folder=None):
    """
    批量处理PNG图片，添加_512后缀并重命名，同时生成200x200的缩略图
    
    参数:
    input_folder (str): 输入文件夹路径
    output_folder (str, optional): 输出文件夹路径，默认为None，表示使用输入文件夹
    """
    # 如果没有指定输出文件夹，使用输入文件夹
    if output_folder is None:
        output_folder = input_folder
    
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 检查文件是否为PNG格式
        if filename.lower().endswith('.png'):
            try:
                # 构建完整的文件路径
                input_path = os.path.join(input_folder, filename)
                
                # 打开图片
                with Image.open(input_path) as img:
                    # 确保图片尺寸为512x512
                    if img.size != (512, 512):
                        print(f"警告: {filename} 的尺寸不是512x512，跳过处理")
                        continue
                    
                    # 获取文件名(不含扩展名)
                    base_name = os.path.splitext(filename)[0]
                    
                    # 构建新的文件名
                    new_name_512 = f"{base_name}_512.png"
                    new_name_200 = f"{base_name}_200.png"
                    
                    # 构建输出路径
                    output_path_512 = os.path.join(output_folder, new_name_512)
                    output_path_200 = os.path.join(output_folder, new_name_200)
                    
                    # 保存512x512的图片
                    img.save(output_path_512, "PNG")
                    print(f"已保存: {new_name_512}")
                    
                    # 创建并保存200x200的缩略图
                    img_200 = img.copy()
                    img_200.thumbnail((200, 200), Image.Resampling.LANCZOS)
                    img_200.save(output_path_200, "PNG")
                    print(f"已保存: {new_name_200}")
            
            except Exception as e:
                print(f"处理文件 {filename} 时出错: {str(e)}")

if __name__ == "__main__":
    # 设置输入文件夹路径
    INPUT_FOLDER = "tmp/"  # 请替换为实际的图片文件夹路径
    
    # 可选: 设置输出文件夹路径，如果不设置则使用输入文件夹
    OUTPUT_FOLDER = "tmp_output/"
    
    # 处理图片
    process_images(INPUT_FOLDER, OUTPUT_FOLDER)    