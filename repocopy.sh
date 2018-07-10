mkdir inrepo
cd inrepo
git clone $1
INDIR=$(ls -d */|head -n 1)
cd ..
mkdir outrepo
cd outrepo
git clone $2
OUTDIR=$(ls -d */|head -n 1)
cd ..
mkdir nbdir
cd nbdir
python smartcopy.py $INDIR $OUTDIR
cd $OUTDIR
git add .
git commit -a -m"Onward"
git push origin master
