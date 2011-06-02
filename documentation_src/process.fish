for file in sourcefiles/*
	echo "Processing: $file"
	python documentationparser.py $file
end
