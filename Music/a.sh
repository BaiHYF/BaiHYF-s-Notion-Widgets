for file in *.mp3; do
  echo "Building widget for $file ..."

    cp -r ./music-widget-template-single ./newmusic
    mv "$file" newmusic/resource/
    
    cd newmusic/build

    ./build.sh

    cd ../..

    NAME=$(cat newmusic/trackname.txt)
    NAME=$(echo "$NAME" | tr -d ' ')

    mv newmusic/ $NAME

    echo "Done building $NAME ..."
done

