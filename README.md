**K-Pop Sexism Detection**

*A repository created for an undergraduate thesis [**"A Semi-Supervised Approach for Sexism Detection in K-Pop Posts"**](https://github.com/aubs7/kpop-sexism/blob/main/Study%20in%20K-pop%20Sexism%20Detection.pdf)*

It contains all the resources used to develop a hybrid model for detecting sexism in K-pop-related posts.
The study utilized a semi-supervised learning approach (pseudolabeling) with stacked embeddings (Glove + FastText), CNN, and Attention mechanism. Overall, the final hybrid model acheived **91.84% accuracy, 90.10% precision, 94.79% recall, 92.38% F1-score, and 96.96% ROC-AUC**. A **web extension** powered by Flask was developed for real-time sexism detection on K-pop posts on Reddit.

⋆｡°✩

This repo primarily features an **unlabeled K-pop-related tweets dataset** for generating pseudolabels. It consists of **11,211** English tweets from popular K-pop scandals and sexist keywords, of which 1,040 came from the Garam bullying scandal generated [Sainez and Wu in 2022](https://github.com/tsainez/kpop-sentiment-analysis), and the 10,171 were manually scraped by [Aubrey Min Lasala](https://github.com/aubs7) & [Britney Beligan](https://github.com/BritneyBeligan) from January to April 2025.

⋆｡°✩

The structure of this repo is as follows:

kpop-sexism/
│
├── 📁 datasets/
│   ├── 📁 for training/
│   │   ├── 📄 train.csv
│   │   ├── 📄 test.csv
│   │   └── 📄 unlabeled.csv *(10,782 rows \\ clean)*
│   │
│   └── 📁 unlabeled/
│       └── 📄 final-scrape.csv *(11,211 rows \\ raw)*
│
├── 📁 model/
│   ├── 📁 src/
│   │   ├── 📄 Baseline Model Training.ipynb
│   │   ├── 📄 SSL Training.ipynb
│   ├── 📄 baseline_model2.h5
│   ├── 📄 kpop-sexism-model2.h5 *(final model)*
│   └── 📄 tokenizer.pickle
│
├── 📁 web-extension/
│   ├── 📄 app.py
│   ├── 📄 preprocessing.py
│   ├── 📁 extension/
│   │   ├── background.js
│   │   ├── index.html
│   │   ├── manifest.json
│   │   ├── script.js
│   │   └── style.css
│
├── 📄 requirements.txt
├── 📄 README.md
└── 📄 Study in K-pop Sexism Detection.pdf

⋆｡°✩

*This repository and its datasets are intended for academic and educational purposes only!*

*Do not use the data, model, or outputs for any harmful, discriminatory, or unauthorized purposes.*

*Happy coding*

