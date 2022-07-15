# Spotify-Million-Playlist-Challenge

> Working on the playlist recommendation system of Spotify using de Million Playlist Dataset

## Project structure

```bash
.
├── data
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   └── raw                         # raw data
├── models                          # store models
├── notebooks                       # all notebooks
│   ├── eda                         # exploratory data analysis
│   ├── evaluation                  # evaluate models and hypothesis
│   └── models                      # model building and training
├── docs                            # documentation for your project
├── .flake8                         # configuration for flake8 - a Python formatter tool
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── .pre-commit-config.yaml         # configurations for pre-commit
├── README.md                       # describe your project
└── src                             # Source code for use in this project.
    ├── __init__.py                 # Makes src a Python module
    ├── data                        # Scripts to download or generate data
    ├── features                    # Scripts to turn raw data into features for modeling
    ├── models                      # Scripts to train models and then use trained models to make predictions
    │   ├── predict_model.py
    │   └── train_model.py
    └── visualization               # Scripts to create exploratory and results oriented visualizations
         └── visualize.py
```
