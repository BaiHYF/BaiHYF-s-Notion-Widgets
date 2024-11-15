#!/bin/bash

mp3_files=( ../resource/*.mp3 )

# 检查是否有 .mp3 文件
if [ ${#mp3_files[@]} -eq 0 ]; then
  echo "No .mp3 files found."
  exit 1
fi

# 改名第一个 .mp3 文件
mv "${mp3_files[0]}" ../resource/music.mp3

# # 删除其他 .mp3 文件
# for file in "${mp3_files[@]:1}"; do
#   rm "$file"
# done

echo "rename_1.sh: Renamed the first .mp3 file to music.mp3 and deleted the rest."