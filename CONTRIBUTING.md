# Welcome!
**To get build of the project on your local environment, as long as you have PyQT5 and the latest(ish) version of Python 3 you should
be able to [clone](https://github.com/selkind/MathSprints) the repository and start the most complete version of the desktop app by running [src/main.py](src/main.py).
Create your own development branch and when you're done, open a PR to merge the branch into master. I will also keep my own active development branch
updated on this repo. I will only merge my own contributions into the master branch once my active developments have reached a relatively stable state**

This project is my hobby. As a developer with very little (16 months) professional experience, it's an opportunity to try building
a piece of software with more than a trivial level of complexity. As a result, while I have tried to maintain good coding practices
and implement common design patterns, the project may have unconventional or simply bad code. 

A very good first contribution would be a stylistic refactor of any code that you think I've done particularly badly.
I'd be very happy to discuss these types of PRs and will do my best to not get defensive. 
I will keep the [issues section](https://github.com/selkind/MathSprints/issues) of this repo updated with current areas of development. These issues will be tagged as [enhancements](https://github.com/selkind/MathSprints/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement). Feel free to open your own
[enhancements or bug reports](https://github.com/selkind/MathSprints/issues/new/choose) and I'll do my best to comment with any pertinent information that comes to mind. However, if you do 
branch off with your own feature or a feature that I've set aside for future development, I may be less actively engaged in your
development (until you submit a PR) in an effort to avoid feature creep.

[SRC/main.py](src/main.py) is the simplest entry point for a whole-project perspective. However, in the [tests](tests) directory, you can find several
other scripts that render individual elements of the GUI or load the application into a state that was previously or is currently
buggy (there may be unittests that specifically test these cases, but I've found that to not be a reliable debugging method).

Currently there are only 2-3 unittest scripts that are "good" tests in that they focus on a single unit of the backend. These 
were created to target the backend classes that have methods that implement core algorithms. These will potentially be refactored
and extended, so test coverage will hopefully help when the time comes. **I do not expect test classes with every contribution**
but knock yourself out if you want!

I have been developing exclusively on Ubuntu, so I'd be interested to hear of any incompatibilities with Windows or Mac.
I'll get around to testing on these platforms eventually, but one of the main reasons for using PyQT as the GUI engine is their
advertised cross-platform capabilities.

For a basic overview of the project, please consult the developer [Wiki](https://github.com/selkind/MathSprints/wiki)
