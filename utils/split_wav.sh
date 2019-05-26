SEGMENT_LENGTH=4  # secs
DIR='data/wav/others_e2'

echo "splitting audio"
for f in $(find $DIR -name '*.wav'); do 
	fn=`echo $f | cut -d \. -f 1`  # drop extension
	sox $f $fn-.wav trim 0 $SEGMENT_LENGTH : newfile : restart
done


echo "remove short segments"
for f in $(find $DIR -name '*.wav'); do 
	length=`soxi -D $f`
	if [ $(echo " $SEGMENT_LENGTH == $length" | bc) -eq 0 ]; then
		rm $f
	fi
done

