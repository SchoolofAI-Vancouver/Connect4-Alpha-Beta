### Alpha-Beta Workshop
This is the starter code for the Alpha Beta Workshop. The Third of a three part series focusing on traditional AI techniques.
This session will focus on improving the MiniMax Algorithm by implementing Alpha-Beta Pruning and Iterative Deepening!

To successfully upgrade minimax you will need to follow the instructions for the following MinimaxPlayer class methods in agents.py:
    
    - search()
    - minimax()
    - min_value()
    - max_value()
    - minimax_search()

### Getting Started
1. Make sure you have [Python 3.6](https://www.python.org/) installed.

2. Clone the repository
    ```bash
    git clone https://github.com/SchoolofAI-Vancouver/Connect4-Minimax.git
    ```
    
3. Use [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) to create a new environment and install dependencies. <br>[Click Here](https://nbviewer.jupyter.org/github/johannesgiorgis/school_of_ai_vancouver/blob/master/intro_to_data_science_tools/01_introduction_to_conda_and_jupyter_notebooks.ipynb) if you need a detail guide on using conda.

    - __Linux__ or __Mac__: 
    ```bash
    conda create --name connect4 python=3.6
    source activate connect4
    conda install numpy
    conda install matplotlib
    conda install jupyter notebook
    ```
  
    - __Windows__: 
    ```bash
    conda create --name connect4 python=3.6 
    activate connect4
    conda install numpy
    conda install matplotlib
    conda install jupyter notebook
    ```

### Instructions
Navigate to the directory and open Connect4.ipynb

    jupyter notebook Connect4.ipynb
