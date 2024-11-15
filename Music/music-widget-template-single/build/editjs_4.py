import csv
from pathlib import Path

def replace_example_name(info_csv_path, script_js_path):
    # 检查文件是否存在
    if not Path(info_csv_path).exists():
        print(f"editjs4: File {info_csv_path} does not exist.")
        return
    if not Path(script_js_path).exists():
        print(f"editjs4: File {script_js_path} does not exist.")
        return

    # 读取 info.csv 文件
    with open(info_csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            row = next(reader)
            new_title = row['Title']
            new_album = row['Album']
        except StopIteration:
            print("editjs4: No valid title found in info.csv.")
            return

    if not new_title or not new_album:
        print("editjs4: No valid title or album found in info.csv.")
        return

    # 读取 script.js 文件内容
    with open(script_js_path, mode='r', encoding='utf-8') as jsfile:
        content = jsfile.read()

    # 替换 "ExampleName" 为 new_title 和 "ExampleAlbum" 为 new_album
    new_content = content.replace('"ExampleName"', f'"{new_title}"')
    new_content = new_content.replace('"ExampleAlbum"', f'"{new_album}"')

    # 生成新的 URL
    new_url = f"./resource/{new_title}.mp3"
    new_content = new_content.replace('"ExampleUrl"', f'"{new_url}"')

    # 写回 script.js 文件
    with open(script_js_path, mode='w', encoding='utf-8') as jsfile:
        jsfile.write(new_content)

    print(f"editjs4: Replaced 'ExampleName' with '{new_title}' in {script_js_path}")

if __name__ == "__main__":
    info_csv_path = Path('../resource/info.csv')
    script_js_path = Path('../script.js')
    
    replace_example_name(info_csv_path, script_js_path)