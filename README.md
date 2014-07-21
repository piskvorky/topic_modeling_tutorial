This repository contains code and instructions for my EuroPython 2014 tutorial, **"Topic Modeling for Fun and Profit"**.

Tutorial setup
==============

Install the following packages **before the training starts**:

```bash
$ pip install six cython numpy scipy ipython[notebook]
$ pip install nltk gensim pattern requests textblob
```

If you run into problems, try to follow the specific packages' installation instructions (e.g. [scipy instructions](http://www.scipy.org/install.html)), ask on their mailing list (don't forget to report your operating system and the actual error) or [contact me](mailto:me@radimrehurek.com), in advance. **There won't be much time for troubleshooting dependencies during the training itself!**

For Windows users, it may be easier to use `conda` to manage the dependencies. Download miniconda from [http://conda.pydata.org/miniconda.html](here), install it, then run:

```bash
$ conda create -n topic_modeling six cython numpy scipy ipython-notebook nltk requests pip
$ source activate topic_modeling
$ pip install nltk pattern gensim textblob
```

Then **download corpora we'll be using for topic modeling and indexing**:

```bash
$ python download_data.py ./data
```

(or, alternatively, download these two files [[14MB](http://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz), [95MB](http://dumps.wikimedia.org/simplewiki/20140623/simplewiki-20140623-pages-articles.xml.bz2)] yourself. No need to unzip them or anything, just copy them under the `./data/` directory of this repository.)

You will need about **700MB of free disk space** to run all the tutorial examples fully.

Check that everything works correctly by opening and running the first tutorial notebook:

```bash
$ ipython notebook '0 - Intro & Setup.ipynb'
```

Congratulations!

Objectives
==========

The tutorial shows how to

* **process very large corpora efficiently**, using practical NLP techniques,
* **automatically extract themes (topics)** from them, using unsupervised topic modeling,
* **index documents** for retrieval and
* **run semantic similarity queries** (*"Give me ten documents that are thematically the most similar to this one."*).

The focus is on building practical applications and engineering, rather than on the theory behind topic modeling and the math itself.

Target audience
===============

This training expects you are a reasonably advanced developer, who knows at least Python basics (dicts, lists, tuples, comprehensions). Knowing NumPy arrays and Python generators/iterators is a plus, but we'll go over what we need.

Same with relevant NLP (natural language processing) and IR (information retrieval) concepts like lemmatization, collocations and unsupervised machine learning (clustering): I'll cover what we need during the training.

How it works
============

Get this repository either via standard `git clone https://github.com/piskvorky/topic_modeling_tutorial.git`, or by downloading and unzipping [this ZIP file](https://github.com/piskvorky/topic_modeling_tutorial/archive/master.zip).

The training materials are a set of IPython notebooks.

To run the notebooks interactively, type in shell:

```bash
$ ipython notebook
```

while in the folder of this repository.

This will open a new browser window, listing all the notebooks. Start from the first one, *"0 - Intro & Setup"*, executing each cell in turn by holding down SHIFT+ENTER.

You can also view the notebooks non-interactively (read-only mode), as HTML in your browser (no Python needed):

[0 - Intro & Setup](http://radimrehurek.com/topic_modeling_tutorial/0%20-%20Intro%20%26%20Setup.html)
[1 - Streamed Corpora](http://radimrehurek.com/topic_modeling_tutorial/1%20-%20Streamed%20Corpora.html)
[2 - Topic Modeling](http://radimrehurek.com/topic_modeling_tutorial/2%20-%20Topic%20Modeling.html)
[3 - Indexing and Retrieval](http://radimrehurek.com/topic_modeling_tutorial/3%20-%20Indexing%20and%20Retrieval.html)

These static HTML notebooks also contain rendered cell output, so you can compare your results to mine.

------


(c) 2014 Radim Řehůřek