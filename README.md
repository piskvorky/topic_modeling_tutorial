This repository contains code and instructions for my EuroPython 2014 tutorial, **"Topic Modeling for Fun and Profit"**.

Tutorial setup
==============

Install the following packages **before the training starts**:

```bash
$ pip install six cython ipython[notebook] numpy scipy
$ pip install gensim
```

If you run into problems, try to follow their [installation instructions](http://www.scipy.org/install.html) or [contact me](mailto:me@radimrehurek.com), in advance. There won't be much time for troubleshooting dependencies during the training itself.

For Windows users, it may be easier to use conda to manage the dependencies (SciPy in particular can be a pain to install). Download miniconda from [http://conda.pydata.org/miniconda.html](here), install it, then run:

```bash
$ conda create -n topic_modeling six numpy scipy ipython-notebook pip
$ source activate topic_modeling
$ pip install gensim
```

