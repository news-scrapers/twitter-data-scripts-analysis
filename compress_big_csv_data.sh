
cd data
for i in *.csv; do
    zip $i.zip $i
done

