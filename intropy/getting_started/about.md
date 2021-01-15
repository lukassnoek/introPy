# About this course
This two-week course was created for the Research Master Psychology at the University of Amsterdam. It is part of the four-week course "Programming in Psychological Science", which starts with two weeks of *R* programming, after which students can choose one of two topics for the remaining two weeks: advanced *R* or Python/PsychoPy (this course). As such, this Python/PsychoPy course assumes that students are familiar with *basic* programming concepts (such as conditionals, loops, and functions). In week 1 of this course, we will delve deeper into Python-specifics (at least, compared to *R*) topics such as object-oriented programming and the most important packages for data processing (including *pandas*, *numpy*, and *matplotlib*). In week 2, we will discuss how to use the software package PsychoPy to create experiments using both its graphical interface (the *Builder*) and its Python interface (the *Coder*).

## Tutorials
This website contains information and tutorials about Python and PsychoPy. Each topic/tutorial has its own page. Tutorials are designed with a `(T)` in the menu on the left. The Python tutorials (week 1) were written in Jupyter notebooks, which are embedded as static HTML files on the website. You can, of course, just read through these pages, but Jupyter notebooks really shine when used *interactively*, which allows you to add, change, and run the Python code embedded in these notebooks. To use these notebooks interactively, you can click on the "rocket" button at the top right of the page (see below; note that this button doesn't do anything). This reveals two options: *Binder* and *JupyterHub*. Both allow you to run the notebooks interactively, but the latter is only available to students of the Research Master Psychology. JupyterHub and Jupyter notebooks are explained in more detail [here](jupyter.md).

<button id="dropdown-buttons-trigger" class="btn btn-secondary topbarbtn"
    aria-label="Launch interactive content"><i class="fas fa-rocket"></i></button>

The tutorials from week 2 are about PsychoPy and are not written in Jupyter notebooks. Instead, they are simply embedded as (static) pages on this website, which contain explanations about the material *and* plenty of exercises! 

Note that we provide both the tutorials and the associated solutions. In the folder with course materials you downloaded, they are located in the folders *tutorials* and *solutions*, respectively. The solutions are exactly the same as the tutorial notebooks, except that they contain the solution embedded between `### BEGIN SOLUTION` and `### END SOLUTION` identifiers. The solutions for the week 2 tutorials are files that contain the full implementation of the tutorial experiments (in `psyexp` files for Builder experiments and regular Python files for Coder experiments).

## Availability of materials
All material from this course (except for the assignments, see below) is open-source and available under the [BSD 3-clause license](https://github.com/lukassnoek/introPy/blob/master/LICENSE). This allows redistribution and use, with or without modification, as long as proper attribution is given (see below). We would love it when others would use this material!

Although all tutorials are publicly available in the course's [Github repository](https://github.com/lukassnoek/introPy), we do not publish the course's assignments as this would enable students to start working on them before they are allowed to do so (and to share the answers). There are two assignments: one Jupyter notebook with several graded exercises testing the students' Python, Pandas, and Matplotlib skills (week 1) and one extensive description of a PsychoPy experiment students have to implement using the PsychoPy Coder interface (week 2).

If you'd like to get access to these assignments, please send Lukas an email (his email address can be found on his [website](https://lukas-snoek.com/)).

## Mistakes, errors, bugs
Although the course materials are tested regularly, they likely still contain mistakes, (spelling) errors, and bugs. You can raise an issue or suggest and edit by clicking on the Github button (see below) on the top of each page. 

<button id="dropdown-buttons-trigger" class="btn btn-secondary topbarbtn"
        aria-label="Connect with source repository"><i class="fab fa-github"></i></button>

For more information about contributing, check out [this page](../misc/CONTRIBUTING.md).

## Acknowledgements
The course material was developed by Lukas Snoek with help from Emma Schreurs. The Python tutorials were adapted from the [*NI-edu* course](https://neuroimaging-uva.github.io/NI-edu/), also taught at the Research Master Psychology (by Lukas Snoek, H. Steven Scholte, Noor Seijdel, and Jessica Loke). The PsychoPy tutorials are in part based on the [PsychoPy workshop](https://nbviewer.jupyter.org/github/gestaltrevision/python_for_visres/blob/master/index.ipynb) from the [GestaltReVision group](http://gestaltrevision.be/en/) at KU Leuven and the materials from PsychoPy's own [3-day workshop](https://workshops.psychopy.org/3days/materials.html). If you ever use PsychoPy in your experiments, please give the PsychoPy developers credit by citing them {cite}`peirce2019psychopy2`.

The exercises in Jupyter notebook tutorials were created using the [nbgrader](https://nbgrader.readthedocs.io/en/stable/) package {cite}`hamrick2016creating`. This website was created using the awesome [Jupyter book](https://jupyterbook.org/) package.

## Attribution
Lukas Snoek. (2020, December 24). lukassnoek/introPy: A Python and PsychoPy course (Version v0.1.0). Zenodo. http://doi.org/10.5281/zenodo.4392860