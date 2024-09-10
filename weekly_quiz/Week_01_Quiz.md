# EODS-F24 Week 1 Quiz

*** Not to be submitted or graded ***

Note: Below, commands beginning with `$` indicate execution at the command line. You don't need to enter this character. Your terminal prompt may end in something different, like a `>`.

## Part 1: Install git and Clone the Course Repo

1. If you don't already have git installed, download and install git from https://git-scm.com/downloads

2. Open a command line terminal:
    - Windows: Start -> Git Bash
    - MacOS: Command+Space -> "Terminal"
    - Linux: Terminal

3.   Navigate to a folder where you keep your projects. Example:

        $ cd /home/your_name/proj/

24
4.  Clone the course repo from https://github.com/AndiCupallariCU/eods-f2024.git

        $ git clone https://github.com/AndiCupallariCU/eods-f2024.git

---


## Part 2: Install Anaconda Python, Create the course Environment and Create a Jupyter Notebook

1. Download and install Anaconda 3 Individual Edition from https://www.anaconda.com/products/distribution

    - Windows: 64-Bit Graphical Installer
    - MacOS: (recommended) 64-Bit Command Line Installer
    - Linux: 64-Bit (x86) Installer

    Follow the instructions here for your os: https://docs.anaconda.com/anaconda/install/
    (recommended) “Do you wish the installer to initialize Anaconda3 by running conda init?” : “yes”. 

2. Open a new command line terminal
    - Windows: Start -> Anaconda Prompt (Anaconda3)
    - MacOS: Command+Space -> "Terminal"
    - Linux: Terminal

3. Navigate to where you cloned the course repo
    
        (base) $ cd ~/proj/eods-f24

4. If you are in the base anaconda environment, you should see `(base)` in the shell prompt (see example above).
If you don't see `(base)`, activate the base environment with:
    
        $ conda activate
    
5. Create a new virtual environment using the requirements file:

        (base) $ conda env create -f requirements.yml

6. Activate the new environment

        (base) $ conda activate eods-f24

7. Add the new environment to jupyter as a kernel

        (eods-f24) $ python -m ipykernel install --user --name eods-f24
        
8. Return to the base environment and launch Jupyter Notebook server

        (eods-f24) $ conda deactivate
        (base) $ jupyter notebook

9. In Jupyter, navigate to the folder: weekly_quiz/

10. Open a new notebook using the newly created kernel: New -> eods-f24

11. Rename the notebook "Week_01_Quiz-UNI", replacing UNI with your uniqname, eg Week_01_Quiz-brg2130

12. In the first cell, copy the following code and run:

        import sys
        import pandas
        import sklearn
        print('python version:',sys.version)
        print('pandas version:',pandas.__version__)
        print('sklearn version:',sklearn.__version__)
        print('pandas path:',pandas.__path__)


