import sys
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
import csv

def parse_mp3_metadata(file_path):
    # 解析 MP3 文件的元数据
    audio = EasyID3(file_path)
    
    # 提取歌名、作者、专辑名
    title = audio.get('title', ['Unknown'])[0]
    artist = audio.get('artist', ['Unknown'])[0]
    album = audio.get('album', ['Unknown'])[0]
    print("res_2.py: Parsed metadata: ", title, artist, album)
    
    with open('../trackname.txt', 'w', encoding='utf-8') as txtfile:
        txtfile.write(title)

    # 输出到 info.csv，以 CSV 格式
    with open('../resource/info.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Artist', 'Album']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        print("res_2.py: Writing metadata to info.csv")
        writer.writeheader()
        writer.writerow({'Title': title, 'Artist': artist, 'Album': album})
    
    # 解析封面图片
    audio_id3 = ID3(file_path)
    for tag in audio_id3.getall('APIC'):
        if tag.mime == 'image/jpeg' or tag.mime == 'image/png':
            with open('../resource/cover.png', 'wb') as img_file:
                img_file.write(tag.data)
            break

if __name__ == "__main__":
    file_path = "../resource/music.mp3"
    parse_mp3_metadata(file_path)
    print("res_2.py: Metadata and cover image saved successfully!")