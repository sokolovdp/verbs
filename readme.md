# CodeAnalysator

**codeanalysator.py** checks folder (or GitHub repo) with source code files to check usage 
of english verbs and nouns in functions and variables names.
Results of analysis can be printed to console, or dumped into the file in CSV 
or JSON format. 

## Usage
```
usage: codeanalysator.py [-h] (--repo REPO | --dir FOLDER) [--ext CODE_EXT]
                         [--top MAX_TOP] [--out OUT_TYPE]

analyses use of verbs and noon in variables and functions names

optional arguments:
  -h, --help      show this help message and exit
  --repo REPO     github(or gist) public repo URL to clone and analyse
  --dir FOLDER    folder with code to analyse
  --ext CODE_EXT  extension of files with code
  --top MAX_TOP   number of top used words, default=5
  --out OUT_TYPE  out results to JSON file, CSV file, or CONsole
```

## Sample output when run as standalone program
```
python codeanalysator.py --dir=test --out=con --ext=.py

Totals
top verbs in func -> ('get' 5) ('load' 3) ('make' 2) ('scrape' 2) ('remove' 1)
top nouns in func -> ('page' 6) ('proxy' 3) ('rating' 2) ('response' 2) ('current' 1)
top verbs in vars -> ('log' 2) ('load' 2) ('sleep' 2) ('search' 1) ('live' 1)
top nouns in vars -> ('url' 13) ('movie' 10) ('page' 5) ('rating' 4) ('proxy' 4)
Details
test\cinemas.py
top verbs in func -> ('get' 5) ('scrape' 2) ('print' 1) ('load' 1) ('create' 1)
top nouns in func -> ('page' 6) ('rating' 2) ('main' 1) ('movie' 1) ('id' 1)
top verbs in vars -> ('log' 2) ('search' 1) ('load' 1) ('list' 1)
top nouns in vars -> ('movie' 6) ('page' 5) ('rating' 3) ('url' 3) ('text' 3)
test\constants.py
top verbs in func -> 
top nouns in func -> 
top verbs in vars -> ('sleep' 2)
top nouns in vars -> ('url' 5) ('movie' 4) ('pattern' 4) ('id' 1) ('title' 1)
```

## Requirements
```
python>=3.6.1
nltk==3.2.4
chardet==3.0.4
To load code from GiHub, local Git client must be installed !
```

## NLTK and WORDNET dictionary installation
```
pip install nltk
```
Then install **wordnet** dictionary through **nltk.download()**
```
python
>>>nltk.download()
>>>exit()
```

