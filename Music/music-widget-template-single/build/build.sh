#!/bin/bash

# 1. 执行 ./rename_1.sh
echo "rename_1.sh..."
./rename_1.sh
if [ $? -ne 0 ]; then
  echo "Error: ./rename_1.sh failed. Exiting."
  exit 1
fi

# 2. 执行 python3 ./parse_2.py
echo "Executing parse_2.py..."
python3 ./parse_2.py
if [ $? -ne 0 ]; then
  echo "Error: python3 ./parse_2.py failed. Exiting."
  exit 1
fi

# 3. 执行 python3 ./renamemp3_3.py
echo "Executing renamemp3_3.py..."
python3 ./renamemp3_3.py
if [ $? -ne 0 ]; then
  echo "Error: python3 ./renamemp3_3.py failed. Exiting."
  exit 1
fi

# 4. 执行 python3 ./editjs_4.py
echo "Executing editjs_4.py..."
python3 ./editjs_4.py
if [ $? -ne 0 ]; then
  echo "Error: python3 ./editjs_4.py failed. Exiting."
  exit 1
fi

echo "Build successfully."