# introPy
Materials for a 2 week Python course taught at the Research Master Psychology (University of Amsterdam). Please to go [https://lukas-snoek.com/introPy](https://lukas-snoek.com/introPy) for more information.  

The documentation was created using [Jupyter Book](https://jupyterbook.org/intro.html).

## Information for educators
All material from this course (except for the assignments, see below) is open-source and available under the [BSD license](https://github.com/lukassnoek/introPy/blob/master/LICENSE). This allows redistribution and use, with or without modification, as long as proper attribution is given (see below).

## Assignments
Although all tutorials are publicly available, we do not publish the course's graded assignments as this would enable students to start working on them before they are allowed to do so (and to share the answers). There are two assignments: one Jupyter notebook with several graded exercises testing the students' Python, Pandas, and Matplotlib skills (week 1) and one extensive description of a PsychoPy experiment students have to create using the PsychoPy Coder (week 2).

If you'd like to get access to these assignments, please send Lukas an email (his email address can be found on his [website](https://lukas-snoek.com/)).

## Mistakes/bugs/etc.
It's very likely that this course contains (spelling) mistakes, inaccuracies, bugs, or other issues related to the text or code in the material. If you find such an issue, please let me know by submitting an issue on, or better yet, submit a pull request with your proposed fix to the issue! Your help is most welcome.

## Attribution
To add: Zenodo DOI.

## Using `nbgrader`
We use [nbgrader](https://nbgrader.readthedocs.io/en/stable/) to convert the *solution* notebooks (which contain the solutions to the exercises) to the *tutorial* notebooks (without the solutions). If you do this yourself, make sure you use the `nbgrader_config.py` file from this repository (because we use the directory names "solutions" and "tutorials" instead of "source" and "release"). 

To regenerate the notebooks from week 1 (week 2 doesn't have any notebooks), run in the root of this repository the following command:

```
nbgrader generate_assignment --force week_*
```

## Testing
To test the notebooks, run the following (note: needs the packages `pytest` and `nbval`):

```
./test_material
```