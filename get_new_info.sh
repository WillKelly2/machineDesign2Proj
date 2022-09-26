touch singularityFNs.txt
echo "# Shaft 1 functions and values" > singularityFNs.txt
python shaft1Design.py >> singularityFNs.txt
echo "# Shaft 2 functions and values" >> singularityFNs.txt
python shaft2Design.py >> singularityFNs.txt
echo "# Shaft 3 functions and values" >> singularityFNs.txt
python shaft3Design.py >> singularityFNs.txt
echo "# Shaft 4 functions and values" >> singularityFNs.txt
python shaft4Design.py >> singularityFNs.txt
cp -rf pdfs /mnt/c/Users/willi/Documents/pdfs