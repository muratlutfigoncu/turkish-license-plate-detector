
for i in *.JPG; do
    printf "Resize $i\n"
    convert "$i" -resize 200x200 "$i"
done
