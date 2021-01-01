## No-collision Transportation Maps

#### This is the repository for the paper "No-collision Transportation Maps", by L. Nurbekyan, A. Iannantuono and A. M. Oberman.

### Approximating optimal transportation maps using k-d trees.

Code to reproduce the methods of the aforementioned [paper](https://arxiv.org/abs/1912.02317). Included are:
* Example script for typical usage
* Algorithm used build k-d tree used to construct the map
* Testing scripts to generate results and perform a comparison

#### Experiments

Building k-d trees for constructing no-collision transportation maps were compared to methods implemented in the Python Optimal Transport (POT) library available [here](https://github.com/rflamary/POT/).

#### Prerequisites

The code was developed and tested in Python 3.7.1, NumPy 1.16.3 and SciPy 1.3.0, although it _should_ work with earlier versions. Comparisons were done using POT 0.5.1.

#### Installing

Download the files or fork the repository, and then run ``example.py``.

#### Code Author

* [Alexander Iannantuono](https://github.com/armeehn) - Development and experimental testing

#### Bugs

If a bug is found, feel free to contact me or create an issue.

#### Acknowledgements

I would like to thank:
* [NSERC](https://www.nserc-crsng.gc.ca/) and [FRQNT](http://www.frqnt.gouv.qc.ca/accueil) for financial support
* The [POT team](https://pot.readthedocs.io/en/stable/#acknowledgements) for their library

#### Citation

If you use these methods in your scientific work, please cite as

    @misc{nurbekyan2019nocollision,
        title={No-collision Transportation Maps},
        author={Levon Nurbekyan and Alexander Iannantuono and Adam M. Oberman},
        year={2019},
        eprint={1912.02317},
        archivePrefix={arXiv},
        primaryClass={math.OC}
    }
