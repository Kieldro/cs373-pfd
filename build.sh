# file variables
source="PFD.py"
unit="TestPFD.py"
inFile="RunPFD.in"
outFile="RunPFD.out"
noError=false


echo RUNNING UNIT TESTS...
python $unit &> TestPFD.out

if ([ $? == 0 ]); then
	echo RUNNING SOURCE...
	python $source < $inFile > $outFile

	#echo CHECKING OUTPUT...; diff -lc RunPFD.out jwilke-RunPFD.out

	echo GENERATING COMMIT LOG...
	git log > PFD.log

	echo UPDATING SPHERE FILE...
	cp $source Sphere$source

	echo RUNNING PYDOC...
	pydoc -w ./$source

<<MULTICOMMENT
	#echo ZIPPING FILE...
	
	
# multicomment cannot have leading spaces
MULTICOMMENT

fi
