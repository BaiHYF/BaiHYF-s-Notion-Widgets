import csv
import os

def rename_music_file(info_csv_path, music_file_path):
    # 读取 info.csv 文件
    with open(info_csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row['Title']
            if title:
                new_file_name = f"{title}.mp3"
                new_file_path = os.path.join(os.path.dirname(music_file_path), new_file_name)
                
                # 检查目标文件是否存在，如果存在则不进行重命名
                if os.path.exists(new_file_path):
                    print(f"renamemp3_3.py: File {new_file_path} already exists. Skipping renaming.")
                else:
                    os.rename(music_file_path, new_file_path)
                    print(f"renamemp3_3.py: Renamed {music_file_path} to {new_file_path}")
                break  # 只处理第一行

if __name__ == "__main__":
    info_csv_path = '../resource/info.csv'
    music_file_path = '../resource/music.mp3'
    
    if not os.path.exists(info_csv_path):
        print(f"File {info_csv_path} does not exist.")
    elif not os.path.exists(music_file_path):
        print(f"File {music_file_path} does not exist.")
    else:
        rename_music_file(info_csv_path, music_file_path)
