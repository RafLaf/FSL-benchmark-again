# Oops, I Sampled it Again:  Reinterpreting Confidence Intervals in Few-Shot Learning

This repository is an implementation of our submission "Oops, I Sampled it Again:  Reinterpreting Confidence Intervals in Few-Shot Learning"
You can cite this work using:
@article{lafargue2024oops,
  title={Oops, I Sampled it Again: Reinterpreting Confidence Intervals in Few-Shot Learning},
  author={Lafargue, Raphael and Smith, Luke and Vermet, Franck and L{\"o}we, Mathias and Reid, Ian and Gripon, Vincent and Valmadre, Jack},
  journal={arXiv preprint arXiv:2409.02850},
  year={2024}
}

This repository is a fork of the [implementation](https://github.com/Frankluox/CloserLookAgainFewShot.git) of ICML 2023 paper: [A Closer Look at Few-shot Classification Again](https://arxiv.org/abs/2301.12246), as well as a Pytorch implementation of [Meta-Dataset](https://github.com/google-research/meta-dataset) without any component of TensorFlow.

We modified the sampler to only sample without replacement. Comparision with the predominent method was performed on the original branch of the repo.
To recreate the experiments, follow the step below.

You can compare your performance to our results. In order to ensure a correct task to task comparision check the results folder and measure correlation with your results. 


# Installation
Install packages using pip:
```bash
$ pip install -r requirements.txt
```

# Datasets
Please follow instructions on the [orginal repository](https://github.com/Frankluox/CloserLookAgainFewShot.git)


# Preparing config files:
The config files for the benchmark can be found in .config/benchmark but you can recreate them using 

```bash
$ python loop_yaml.py
```

# Running the scripts:
you can then run the scripts by selecting which backbone you prefer and the number of shots:
```bash
./loop_exp.sh clip 10
```
It will test every datasets and store the results in the folder specified in loop_exp.sh.


