# Running Decision Tree on TigerGraph
This repository contains code that allows you to run classification of vertices in TigerGraph using a decision tree that is loaded into the graph.

## Setup
Create a custom ```config.json``` file that follows the same format as ```config-template.json``` that contains your specific url and authentication details.

## Data
Data comes from a dataset hosted on Kaggle, found [here](https://www.kaggle.com/prakharrathi25/banking-dataset-marketing-targets). It is encouraged to read through the dataset information on the Kaggle page, but the dataset is a classification problem if a given customer is going to use a bank product.

## Running the schema creation, data loading, and query installation
With the correct python packages installed and your config.json created, run ```python main.py -a``` to create the schema, load the data, and install the classification query.
