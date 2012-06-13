# file variables
python=true

source="PFD.py"
inFile="RunCollatz.in"
outFile="RunCollatz.out"
compile=false
grep=false
noError=false

echo RUNNING UNIT TESTS...
#python TestCollatz.py &> TestCollatz.py.out

echo RUNNING SOURCE...
python $source < $inFile > $outFile

echo CHECKING OUTPUT...
#diff -lc RunCollatz.out RunCollatz.in

<< '--MULTICOMMENT--'

free 
comments!
--MULTICOMMENT--

echo GENERATING COMMIT LOG...
git log > Collatz.log

echo UPDATING SPHERE FILE...
cp $source Sphere$source

echo RUNNING PYDOC...
pydoc -w ./$source

#echo ZIPPING FILE...

