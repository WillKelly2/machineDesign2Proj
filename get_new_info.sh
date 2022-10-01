touch singularityFNs.txt
x="0.61"
python shaft1Design.py $x> pdfs/singularityFNs1.txt
python shaft2Design.py $x> pdfs/singularityFNs2.txt
python shaft3Design.py $x> pdfs/singularityFNs3.txt
python shaft4Design.py $x> pdfs/singularityFNs4.txt
python extractdata.py

cp -rf pdfs /mnt/c/Users/willi/Documents/pdfs