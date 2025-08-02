---
title: "DAIR-3, Day 2: Building Robust ML Models"
---

# {{ page.title }}

**Date**: August 5th, 2025, from 8:30-11:45AM
<br>**Instructor**: [Suraj Rampure](../) (rampure@umich.edu)
<br>[Program Website](https://midas.umich.edu/events/dair-sa-2025/)

_In this session, we will review the basics of predictive modeling and approaches to build an accurate and reproducible model, introduce best practices in reporting that will allow others to appropriately interpret and reproduce the results, and discuss guiding principles on how to reproduce others’ results._

<div style="border: 2px solid #f39c12; background-color: #fcf3cf; padding: 16px; border-radius: 6px; margin-bottom: 16px;">
  <strong>Please fill out the <a href="https://forms.gle/keWxV9aieckgqoZb7" target="_blank">Welcome Survey</a> before the session begins.</strong>
</div>

<br>

There are four Python-based Jupyter Notebooks for this session.

1. **Overview of Machine Learning and Tools** (Jupyter Notebooks, `sklearn`, Logistic Regression, Train-Test Splits)
2. **Dimensionality Reduction** (Random Seeds, Stratification, PCA, MDS, t-SNE)
3. **Model Selection** (Cross-Validation, Regularization, Feature Standardization, Data Leakage)
4. **Model Evaluation** (Precision, Recall, ROC-AUC, More on Class Imbalance)

Don't worry if you're not familiar with Python – most of the code is already provided for you. Instead, focus on understanding the concepts and the code that's provided.

There are two ways to access these notebooks. To get the most out of the workshop, I recommend you follow at least one of them, so that you can run code and experiment yourself.

### Option 1: Web-Based Access

<div style="border: 2px solid #2980b9; background-color: #d6eaf8; padding: 16px; border-radius: 6px; margin-bottom: 16px;">
  <strong>Click <a href="https://mybinder.org/v2/gh/surajrampure/dair3-2025/HEAD?urlpath=%2Fdoc%2Ftree%2F01-intro-materials.ipynb" target="_blank">here</a> to open the notebooks in your browser, without the need to install anything.</strong>
</div>

 This link uses [mybinder.org](https://mybinder.org/), a service that allows you to run Jupyter Notebooks in your browser. Some code may not work properly or take a long time to run, but this should suffice for the workshop.

<br>

### Option 2: Local Installation

You can also clone our GitHub repository and run the notebooks locally. This option is suggested if you've used Jupyter Notebooks locally before, but if you haven't, the web-based option is probably easier.

Find the repository [**here**](https://github.com/surajrampure/dair3-2025). There is a `requirements.txt` file in the repository that you can use to install the necessary dependencies.

In your Terminal, run the following commands:

```bash
git clone https://github.com/surajrampure/dair3-2025.git
cd dair3-2025
pip install -r requirements.txt
cd files
```

You can then open the notebooks in your browser by running `jupyter notebook` in your Terminal.

If you'd like more detailed steps on how to run Jupyter Notebooks locally, refer to [**this guide**](https://practicaldsc.org/env-setup/#replicating-the-gradescope-environment).