# The Original Problem

![](graphics/original_mit_crew-01.png)

The thing we're going to learn about in this course, **computer vision**, has a very interesting history. It's roots really go all the way back to the beginning of computing and **artifical intelligence.** When this course is over, I want you to understand where we **really** are today, how we got here, and be able to make some reasonable conjectures about where the field is going next. 

I want you to be comfortable with cutting edge deep learning techniques, but also understand the broader context to which they belong. I want you to really understand why it's so deceptively difficult to program a computer to anything remotely close to what our visual cortex does. 

To acheive this, we need to go back to the beginning. Not the very beginning, but pretty close. We need to go back to MIT in the summer of 1966 and visit the **Artifical Intelligence Group.**

## Using this Repository

This repository is notebook focused. The name of each notebook begins with a number indicating the order they should be read or presented in. 

## Setup 

The Python 3 [Anaconda Distribution](https://www.anaconda.com/download) is the easiest way to get going with the notebooks and code presented here. 

(Optional) You may want to create a virtual environment for this repository: 

~~~
conda create -n cv python=3
source activate cv            # or just 'activate cv' in Windows
~~~

You'll need to install the jupyter notebook to run the notebooks:

~~~
conda install jupyter

# You may also want to install nb_conda (Enables some nice things like change virtual environments within the notebook)
conda install nb_conda
~~~

This repository requires the installation of a few extra packages, you can install them all at once with:
~~~
pip install -r requirements.txt
~~~

(Optional) [jupyterthemes](https://github.com/dunovank/jupyter-themes) can be nice when presenting notebooks, as it offers some cleaner visual themes than the stock notebook, and makes it easy to adjust the default font size for code, markdown, etc. You can install with pip: 

~~~
pip install jupyterthemese
~~~

Recommend jupyter them for presenting these notebook (Type into terminal before launching notebook):

~~~
jt -t grade3 -cellw=90% -fs=20 -tfs=20 -ofs=20 -dfs=20
~~~



### Downloading Data
For larger files such as data and videos, I've provided download scripts to download these files from welchlabs.io. These files can be pretty big, so you may want to grab a cup of your favorite beverage to enjoy while downloading. The script can be run from within the jupyter notebooks or from the terminal:

~~~
python util/get_and_unpack.py -url http://www.welchlabs.io/unccv/the_original_problem/data/data.zip
~~~

Alternatively, you can download [download data manually](http://www.welchlabs.io/unccv/the_original_problem/data/data.zip), unzip and place in this directory. 


### Downloading Videos

Run the script below or call it from the notebooks:

~~~
python util/get_and_unpack.py -url http://www.welchlabs.io/unccv/the_original_problem/videos.zip
~~~

Alternatively, you can download [download videos manually](http://www.welchlabs.io/unccv/the_original_problem/videos.zip), unzip and place in this directory. 


## Programming Challenge

