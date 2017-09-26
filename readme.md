# verbs_usage

**codeanalysator.py** check folder with source code files to check usage 
of english verbs and nouns in functions and variables names
Results of analysis can be printed to console, or dumped into the file in CSV 
or JSON format. 

## Usage
```
usage: codeanalysator.py [-h] [--ext CODE_EXT] [--top MAX_TOP] [--vb] [--nn]
                         [--vrbl] [--func] [--out OUT_TYPE]
                         folder

analyses use of verbs and noon in variables and functions names

positional arguments:
  folder          folder with code to analyse

optional arguments:
  --help          show this help message and exit
  --ext CODE_EXT  extension of files with code
  --top MAX_TOP   number of top used words
  --vb            check usage of verbs
  --nn            check usage of nouns
  --vrbl          check variables names
  --func          check functions names
  --out OUT_TYPE  out results to JSON file, CSV file, or CONsole

```

## Sample output when run as standalone program
```
Totals:
=======
top verbs in func: [('get', 21), ('list', 13), ('load', 11), ('fetch', 9), ('output', 8), ('create', 6), ('parse', 5)]
top nouns in func: [('page', 16), ('user', 9), ('movie', 8), ('rating', 8), ('console', 6), ('sort', 4), ('file', 4)]
top verbs in vars: [('list', 19), ('count', 14), ('search', 4), ('out', 2), ('load', 2), ('log', 2), ('sleep', 2)]
top nouns in vars: [('movie', 35), ('url', 27), ('film', 20), ('page', 19), ('rating', 13), ('raw', 12), ('id', 11)]
Details:
========
   test\cinemas.py:
     top verbs in func: [('get', 5), ('scrape', 2), ('load', 1), ('make', 1), ('print', 1), ('create', 1)]
     top nouns in func: [('page', 6), ('rating', 2), ('response', 1), ('movie', 1), ('id', 1), ('url', 1), ('year', 1)]
     top verbs in vars: [('log', 2), ('load', 1), ('list', 1), ('search', 1)]
     top nouns in vars: [('movie', 6), ('page', 5), ('text', 3), ('url', 3), ('rating', 3), ('year', 2), ('file', 2)]
```


## Requirements
```
python>=3.6.1
nltk==3.2.4
chardet==3.0.4
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

