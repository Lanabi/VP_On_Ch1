The instruction below outlines:

	1. Preprocessing: Scarping
	2. Preprocessing: Labelling
		2.1. File preparation
		2.2. Labelling with Ruber-tiny
		2.3. Labelling with Newsmap
		2.4. Comparing the labels
	3. Analysis 
	4. Environment

1. Preprocessing: Scarping

Scraping included two stages. In the initial stage, I executed 'js_scraper.py,' which locally saved the JavaScript files containing the links to all the news reports from the website. An example of one of these files (2760.js) is provided in the folder. Next, I ran 'news_scraper.ipynb,' that collected the links to the news reports from all the JavaScript files, scraped the title, text, and date of a news episode for each link, and saved these data into a Python pandas DataFrame. 

The entire process required approximately one month to execute the scraper.
The resulting corpus, trimmed to the period from 31 December 1999 until February 23, 2022, is on dataverse:
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZU1T0C

The dataframe includes the following columns:

	'dates': date of a news episode
	'text': title and text of a news episode
	'country': county-label assigned by Newsmap
	'sentiment_labels': sentiment-label assigned by Rubert-tiny
	'sentiment_score': sentiment score assigned by Rubert-tiny

Files related to scraping:
Input:
	js_scraper.py
	news_scraper.ipynb
Output:
	2760.js
	corpus.pkl (needs to be dowloaded from dataverse, the link is above)

2. Preprocessing: Labelling

The preprocessing was also conducted in two stages. Ruber-tiny (in Python) was used to assign 'sentiment label' (positive, negative, or neutral) and ''sentiment score'. Newsmap (in R) was used to assign country-topics.

Below, I explain how to reporduct the labelling

2.1. File preparation 

To reproduce the labeling, you will need to create two files: 'corpus_for_newsmap.feather' and 'corpus_for_rubert.pkl'. These files can be created using the dataset downloaded from Dataverse (corpus.pkl) and preprocessing.ipynb. Please open preprocessing.ipynb and follow the instructions.

Input:
	corpus.pkl (can be dowloaded from dataverse)
	preprocessing.ipynb

Output:
	corpus_for_rubert.pkl
	corpus_for_newsmap.feather

2.2. Labelling with Ruber-tiny

The script for labelling with r

The file corpus.pkl has been labelled by Rubert-tiny.
The process required approximately 8 hours to execute. Update: It took 9.5 hours last time, but the machine was running other processes simultaneously.

Files related to the labelling:	
	rubert.py

2.3. Labelling with Newsmap

The file corpus.pkl was saved as a Feather file to be readable in R (the code to save a pickled file to a Feather file is provided in the last line of analysis.ipynb). Following that, the file was labeled by Newsmap in R. Please note that the labels were assigned based on a larger dataset (spanning from 1998-12-23 until 2022-06-20). Following the comments by the reviewers, the dataset was trimmed to a shorter period (from 1999-12-31 until 2022-02-23). Further checks suggest that training Newsmap for this shorter period results in slightly different labels (2% of mismatches with the original labels).

The process required approximately 37 minutes to execute.
Files related to the labelling:
	newsmap_training.R
	cities.csv (dictionary)

2.4. Comparing labels

The stage below explains how to compare the lables created by Rubert-tiny and Newsmap.

3. Analysis

The analysis, including the figures, tables, and other numbers reported in the article and the appendix, can be reproduced with the file 'analysis.ipynb'. The file also provides an overview of the dataset. 

Related files:
	analysis.ipynb
	corpus.pkl
	validation.csv

4. Environment

OS version:
macOS-10.16-x86_64-i386-64bit

Python version:
3.9.13 (main, Aug 25 2022, 18:29:29) 
[Clang 12.0.0 ]

Current Kernel Information:
Python 3.9.13 (main, Aug 25 2022, 18:29:29) 

Installed Packages (report from Jupiter/Anaconda):

Package                      Version
---------------------------- ---------
absl-py                      1.4.0
aiohttp                      3.8.3
aiosignal                    1.2.0
appdirs                      1.4.4
astunparse                   1.6.3
async-timeout                4.0.2
attrs                        22.1.0
blinker                      1.4
boltons                      23.0.0
brotlipy                     0.7.0
cachetools                   5.3.0
certifi                      2023.7.22
cffi                         1.15.1
charset-normalizer           2.0.4
click                        8.0.4
conda                        23.3.1
conda-content-trust          0.1.3
conda-package-handling       2.0.2
conda_package_streaming      0.7.0
contourpy                    1.0.7
cryptography                 38.0.4
cycler                       0.11.0
distlib                      0.3.6
dostoevsky                   0.6.0
fasttext                     0.9.2
filelock                     3.9.0
flatbuffers                  23.1.21
flit_core                    3.6.0
fonttools                    4.39.4
frozenlist                   1.3.3
gast                         0.4.0
google-auth                  2.16.1
google-auth-oauthlib         0.4.6
google-pasta                 0.2.0
grpcio                       1.51.3
h5py                         3.8.0
idna                         3.4
jsonpatch                    1.32
jsonpointer                  2.1
keras                        2.11.0
Keras-Preprocessing          1.1.2
kiwisolver                   1.4.4
libclang                     15.0.6.1
Markdown                     3.4.1
MarkupSafe                   2.1.2
matplotlib                   3.7.1
matplotlib-venn              0.11.9
mkl-service                  2.4.0
multidict                    6.0.2
numpy                        1.25.2
oauthlib                     3.2.2
opt-einsum                   3.3.0
packaging                    23.0
Pillow                       9.5.0
pip                          22.3.1
platformdirs                 3.0.0
pluggy                       1.0.0
pooch                        1.4.0
protobuf                     3.20.3
pyasn1                       0.4.8
pyasn1-modules               0.2.8
pybind11                     2.10.4
pycosat                      0.6.4
pycparser                    2.21
PyJWT                        2.4.0
pyOpenSSL                    22.0.0
pyparsing                    3.0.9
PySocks                      1.7.1
python-dateutil              2.8.2
razdel                       0.5.0
requests                     2.28.1
requests-oauthlib            1.3.1
rsa                          4.9
ruamel.yaml                  0.17.21
ruamel.yaml.clib             0.2.6
scipy                        1.11.1
setuptools                   65.6.3
six                          1.16.0
tensorboard                  2.11.2
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow                   2.11.0
tensorflow-estimator         2.11.0
tensorflow-io-gcs-filesystem 0.30.0
termcolor                    2.2.0
toolz                        0.12.0
tqdm                         4.64.1
typing_extensions            4.5.0
urllib3                      1.26.6
virtualenv                   20.19.0
Werkzeug                     2.2.3
wheel                        0.35.1
wrapt                        1.14.1
yarl                         1.8.1
zstandard                    0.19.0


R version
               _                           
platform       aarch64-apple-darwin20      
arch           aarch64                     
os             darwin20                    
system         aarch64, darwin20           
status                                     
major          4                           
minor          4.0                         
year           2024                        
month          04                          
day            24                          
svn rev        86474                       
language       R                           
version.string R version 4.4.0 (2024-04-24)
nickname       Puppy Cup   

Installed packages (R)

                   Package              Version     
arrow              "arrow"              "16.1.0"    
assertthat         "assertthat"         "0.2.1"     
base               "base"               "4.4.0"     
bit                "bit"                "4.0.5"     
bit64              "bit64"              "4.0.5"     
boot               "boot"               "1.3-30"    
cellranger         "cellranger"         "1.1.0"     
class              "class"              "7.3-22"    
cli                "cli"                "3.6.2"     
clipr              "clipr"              "0.8.0"     
cluster            "cluster"            "2.1.6"     
codetools          "codetools"          "0.2-20"    
compiler           "compiler"           "4.4.0"     
cpp11              "cpp11"              "0.4.7"     
crayon             "crayon"             "1.5.2"     
datasets           "datasets"           "4.4.0"     
dplyr              "dplyr"              "1.1.4"     
fansi              "fansi"              "1.0.6"     
fastmatch          "fastmatch"          "1.1-4"     
feather            "feather"            "0.3.5"     
foreign            "foreign"            "0.8-86"    
generics           "generics"           "0.1.3"     
glue               "glue"               "1.7.0"     
graphics           "graphics"           "4.4.0"     
grDevices          "grDevices"          "4.4.0"     
grid               "grid"               "4.4.0"     
here               "here"               "1.0.1"     
hms                "hms"                "1.1.3"     
ISOcodes           "ISOcodes"           "2024.02.12"
jsonlite           "jsonlite"           "1.8.8"     
KernSmooth         "KernSmooth"         "2.23-22"   
lattice            "lattice"            "0.22-6"    
lifecycle          "lifecycle"          "1.0.4"     
magrittr           "magrittr"           "2.0.3"     
MASS               "MASS"               "7.3-60.2"  
Matrix             "Matrix"             "1.7-0"     
methods            "methods"            "4.4.0"     
mgcv               "mgcv"               "1.9-1"     
newsmap            "newsmap"            "0.9.0"     
nlme               "nlme"               "3.1-164"   
nnet               "nnet"               "7.3-19"    
nsyllable          "nsyllable"          "1.0.1"     
parallel           "parallel"           "4.4.0"     
pillar             "pillar"             "1.9.0"     
pkgconfig          "pkgconfig"          "2.0.3"     
png                "png"                "0.1-8"     
prettyunits        "prettyunits"        "1.2.0"     
progress           "progress"           "1.2.3"     
proxyC             "proxyC"             "0.4.1"     
purrr              "purrr"              "1.0.2"     
quanteda           "quanteda"           "4.0.2"     
quanteda.textstats "quanteda.textstats" "0.97"      
R6                 "R6"                 "2.5.1"     
rappdirs           "rappdirs"           "0.3.3"     
Rcpp               "Rcpp"               "1.0.12"    
RcppArmadillo      "RcppArmadillo"      "0.12.8.3.0"
RcppTOML           "RcppTOML"           "0.2.2"     
readr              "readr"              "2.1.5"     
readxl             "readxl"             "1.4.3"     
rematch            "rematch"            "2.0.0"     
reticulate         "reticulate"         "1.37.0"    
rlang              "rlang"              "1.1.3"     
rpart              "rpart"              "4.1.23"    
rprojroot          "rprojroot"          "2.0.4"     
SnowballC          "SnowballC"          "0.7.1"     
spatial            "spatial"            "7.3-17"    
splines            "splines"            "4.4.0"     
stats              "stats"              "4.4.0"     
stats4             "stats4"             "4.4.0"     
stopwords          "stopwords"          "2.3"       
stringi            "stringi"            "1.8.4"     
stringr            "stringr"            "1.5.1"     
survival           "survival"           "3.5-8"     
tcltk              "tcltk"              "4.4.0"     
tibble             "tibble"             "3.2.1"     
tidyselect         "tidyselect"         "1.2.1"     
tools              "tools"              "4.4.0"     
tzdb               "tzdb"               "0.4.0"     
utf8               "utf8"               "1.2.4"     
utils              "utils"              "4.4.0"     
vctrs              "vctrs"              "0.6.5"     
vroom              "vroom"              "1.6.5"     
withr              "withr"              "3.0.0"     
xml2               "xml2"               "1.3.6"     
yaml               "yaml"               "2.3.8"     

R Studio version: ‘2024.4.1.748’
