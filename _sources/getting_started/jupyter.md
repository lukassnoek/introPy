# The Jupyter ecosystem
In this course, we will use several tools from *project Jupyter* {cite}`kluyver2016jupyter`. This project includes several nifty tools to make programming a little easier!

## JupyterHub
One tool that we use in this course is "JupyterHub". This piece of software allows you to easily create a preconfigured Python environment on an external server &mdash; no need to install Python on your own computer anymore! You just go to the website/public IP associated with the external server and you can start programming! We run JupyterHub on our own server at the University of Amsterdam, which Research Master students can use for this course. Others may use the aforementioned tool "Binder" to create a JupyterHub instance themselves, which can be used for this course as well!

## JupyterLab
Another tool we use is "JupyterLab", which is an extensive integrated development environment (IDE) similar to RStudio. Because it is implemented in the browser, it combines well with JupyterHub (but it can also be used on your own computer). Using the JupyterLab interface, you can create text files and (Python) scripts, open interactive Python consoles, open terminals, and run so-called Jupyter Notebooks (for more info, check the [documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)). Don't worry if this doesn't make sense to you at this point! We will explain the most important functionality step-by-step during the course.

If you want to see how JupyterLab looks like, click one of the two buttons below, which will launch a Jupyterhub instance with a Jupyterlab interface that includes the course materials. The UvA JupyterHub is only accessible to Research Master Students enrolled in the "Programming for Psychology" course.

[![UvA](https://badgen.net/badge/UvA/Jupyterhub/orange)](https://neuroimaging.lukas-snoek.com)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lukassnoek/introPy/master?urlpath=lab)

Note that, instead of using the JupyterLab interface, you can also use the "classic" interface, which is less extensive but also "cleaner". To do so, click on *Help* &rarr; *Launch Classic Notebook* or change the word `lab` to the word `tree` in the URL. To change back from the classic interface to the Jupyterlab interface, change the word `lab` back to `tree` in the URL. 

:::{note}
If you have installed Python on your own computer, you can start the Jupyterlab interface by clicking on the JupyterLab icon in Anaconda Navigator (Mac/Windows) or running the following command in your terminal (Mac/Linux) or Anaconda prompt (Windows):

    jupyter lab

:::

## Jupyter Notebooks
Finally, we use "Jupyter Notebooks" a lot in this course. Jupyter notebooks are very similar to R Markdown files. Like R Markdown files, you can mix text, code, plots, and mathematical formulas within a single document (see gif below).

![jupyter_gif](https://miro.medium.com/max/2380/1*Y0wfx6EBWAGo_gfmUZHJLw.gif)
*Gif from Cornellius Yudha Wijaya on [towardsdatascience.com](https://towardsdatascience.com/elevate-your-jupyter-notebook-environment-experience-9bdd1101aa54)*

Most of our tutorials are actually written in Jupyter notebooks. These notebooks are great for "interactive programming", in which it is easy to experiment, try out, and troubleshoot your code. Because this mode of programming is great for teaching, we will use Jupyter notebooks a lot in week 1. Interactive programing is not, however, the only way in which you use Python. In fact, a lot of people use Python in a non-interactive way by writing scripts. In this "script mode" (for lack of a better term), writing the code and running the code are done separately. The code interface of PsychoPy, for example, cannot be used interactively and only supports "script mode". We will dicuss both modes in this course.

If you want to check out Jupyter notebooks already, open Jupyterlab (using Binder, on the UvA server, or on your own computer) and click in the launcher on the *Python 3* tile under the *Notebook* header, which will open a new Jupyter notebook!

Now, you should be ready to start on the course materials!