Simplified U-NET implementation for Semantic Segmentation with the M2NIST Dataset.

--------------------
Directory Structure
--------------------

    .
    ├── AUTHORS.md
    ├── README.md
    ├── config  <- any configuration files
    ├── data
    │   ├── processed <- data after all preprocessing has been done
    │   └── raw <- original unmodified data acting as source of truth and provenance
    ├── docs  <- usage documentation or reference papers
    ├── models  <- compiled model .pkl or HDFS or .pb format
    ├── notebooks <- jupyter notebooks for exploratory analysis and explanation 
    ├── reports <- generated project artefacts eg. visualisations or tables
    │   └── figures
    └── src
        ├── data <- scripts for processing data eg. transformations, dataset merges etc. 
        ├── visualization  <- scripts for visualisation during EDA, modelling, error analysis etc. 
        ├── modeling    <- scripts for generating models
    |--- environment.yml <- file with libraries and library versions for recreating the analysis environment

--------------------
"[Multidigit MNIST (M2NIST) Dataset](https://www.kaggle.com/farhanhubble/multimnistm2nist)" by [farhanhubble](https://www.kaggle.com/farhanhubble) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
