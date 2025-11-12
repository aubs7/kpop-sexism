**K-Pop Sexism Detection**

*A repository created for an undergraduate thesis [**"A Semi-Supervised Approach for Sexism Detection in K-Pop Posts"**](https://github.com/aubs7/kpop-sexism/blob/main/Study%20in%20K-pop%20Sexism%20Detection.pdf)*

It contains all the resources used to develop a hybrid model for detecting sexism in K-pop-related posts.
The study utilized a semi-supervised learning approach (pseudolabeling) with stacked embeddings (Glove + FastText), CNN, and Attention mechanism. Overall, the final hybrid model acheived **91.84% accuracy, 90.10% precision, 94.79% recall, 92.38% F1-score, and 96.96% ROC-AUC**. A **web extension** powered by Flask was developed for real-time sexism detection on K-pop posts on Reddit.

⋆｡°✩

This repo primarily features an **unlabeled K-pop-related tweets dataset** for generating pseudolabels. It consists of **11,211** English tweets from popular K-pop scandals and sexist keywords, of which 1,040 came from the Garam bullying scandal generated [Sainez and Wu in 2022](https://github.com/tsainez/kpop-sentiment-analysis), and the 10,171 were manually scraped by [Aubrey Min Lasala](https://github.com/aubs7) & [Britney Beligan](https://github.com/BritneyBeligan) from January to April 2025.

⋆｡°✩

The structure of this repo is as follows:

```text
kpop-sexism/
│
├── 📁 datasets/                                       # All datasets used in the project
│   ├── 📁 for-training/                               # Cleaned datasets for model training
│   │   ├── 📄 train.csv                               # 5,644 rows - cleaned training set
│   │   ├── 📄 test.csv                                # 2,208 - cleaned test set
│   │   └── 📄 unlabeled.csv                           # 10,782 rows – cleaned unlabeled data
│   │
│   └── 📁 unlabeled/                                  # Raw scraped dataset
│       └── 📄 final-scrape.csv                        # 11,211 rows – raw data
│
├── 📁 model/                                          # Model files and training notebooks
│   ├── 📄 baseline_model2.h5                          # Baseline trained model
│   ├── 📄 kpop-sexism-model2.h5                       # Final trained model
│   ├── 📄 tokenizer.pickle                            # Tokenizer for preprocessing
│   └── 📁 src/                                        # Training notebooks and scripts
│       ├── 📄 Baseline_Model_Training.ipynb
│       └── 📄 SSL_Training.ipynb
│
├── 📁 web-extension/                                  # Flask app and browser extension
│   ├── 📄 app.py                                      # Flask backend for real-time detection
│   ├── 📄 preprocessing.py                            # Preprocessing scripts for web input
│   └── 📁 extension/                                  # Browser extension (upload on Google Extensions)
│       ├── 📄 background.js
│       ├── 📄 index.html
│       ├── 📄 manifest.json
│       ├── 📄 script.js
│       └── 📄 style.css
│
├── 📄 system-reqs.txt               
├── 📄 README.md                     
└── 📄 Study_in_K-pop_Sexism_Detection.pdf 


```

⋆｡°✩

Notes:
1. The web extension is designed to work only on **Reddit threads**.
2. train.csv and test.csv contain English labeled data from the [EXIST 2021 dataset](https://nlp.uned.es/exist2021/) and manually annotated K-pop tweets, while unlabeled.csv contains unlabeled K-pop tweets only. They have been cleaned using preprocessing.py.
3. Although preprocessing and data wrangling techniques were applied to clean the for-training/ datasets, some rows may still be messy or uncleaned.

*This repository and its datasets are intended for academic and educational purposes only!*

*Do not use the data, model, or outputs for any harmful, discriminatory, or unauthorized purposes.*

*Happy coding <3*

