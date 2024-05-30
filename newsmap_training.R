# Clear the current R environment to start fresh
rm(list = ls())
# Load necessary libraries/packages
library(quanteda)  # For text analysis and manipulation
library(feather)   # For reading and writing feather files
library(stringr)   # For string manipulation functions
require(newsmap)   # for country-topic classification
library(dplyr)     # For data manipulation and transformations
library(arrow)     # For reading and writing of data files
library(readr)     # For reading delimited files (CSV)
# Get the current working directory
current_dir <- getwd()
# Define paths
path_to_open <- file.path(current_dir, "for_newsmap.feather")
path_to_dict <- file.path(current_dir, "cities.csv")
path_to_save <- file.path(current_dir, "from_newsmap.feather")
# Upload the corpus
dat <- arrow::read_feather(path_to_open)
# Create a corpus from the data 'dat', using the 'text' field
corp <- corpus(dat, text_field = 'text')
# Tokenize the corpus, removing punctuation and numbers
toks <- tokens(corp, remove_punct = TRUE, remove_numbers = TRUE)
# Larger dictionary of toponyms 
cities <- read_csv(path_to_dict)
# Split 'value' column of 'cities' DataFrame by 'countrycode'
lis <- split(cities$value, cities$countrycode)
# Convert the list 'lis' into a dictionary object
dct <- as.dictionary(lis)
# Apply tokens_lookup function to associate tokens with dictionary 'dct'
label_toks <- tokens_lookup(toks, dct, levels = 1, valuetype = "glob")  
# Create a document-feature matrix (DFM) from labeled tokens
label_dfm <- dfm(label_toks)  # Convert 'label_toks' to a DFM
feat_dfm <- dfm(toks, tolower = FALSE)  
# Include only proper nouns into the feature matrix (DFM)
feat_dfm <- dfm_select(feat_dfm, selection = "keep",
                       '^\\p{Lu}', valuetype = 'regex',
                       case_insensitive = FALSE)
# Trim the feature matrix (DFM) by removing terms with frequency less than 1
feat_dfm <- dfm_trim(feat_dfm, min_termfreq = 1)
# Create a NewsMap model using the feature matrix (DFM) and labeled tokens (DFM)
model <- textmodel_newsmap(feat_dfm, label_dfm)
# Display coefficients of the NewsMap model
coef(model, n = 7)
# Prepare prediction data 
pred_data <- data.frame(text_and_title = as.character(corp), 
                        country = predict(model), 
                        date = dat$dates)
# Write prediction data to a feather file 
write_feather(pred_data, path_to_save)

