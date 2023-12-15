# About

Replication dataset for the research paper "A Survey on How Test Flakiness Affects Developers and What Support They Need To Address It", which was presented at the 15th IEEE International Conference on Software Testing, Verification and Validation (ICST) 2022

Here you can find the [pre-print](https://arxiv.org/abs/2203.00483) of the paper.

[plot_dataset.ipynb](plot_dataset.ipynb) shows how to derive the plots from the dataset.


# Execute notebook

Create and activate virtualenv ...

Install requirements
```bash
pip install -r requirements.txt
```

Register virtualenv in jupyter ([reference](https://janakiev.com/blog/jupyter-virtual-envs/))
```bash
python -m ipykernel install --user --name=a-survey
```

Start jupyter notebook and switch kernel via Kernel -> Change kernel -> a-survey
