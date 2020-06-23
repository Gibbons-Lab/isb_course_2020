#!/usr/bin/env python

"""
This script runs a rank sums tests on phylotypes from input case-control data
"""

__author__ = "Sean Gibbons and Christian Diener"
__copyright__ = "Copyright 2017"
__credits__ = ["Sean Gibbons; Christian Diener"]
__reference__ = ("PLoS Computational Biology DOI: "
                 "https://doi.org/10.1371/journal.pcbi.1006102")
__license__ = "GPL"
__version__ = "1.0.0-dev"
__maintainer__ = "Sean Gibbons"
__email__ = "sgibbons@systemsbiology.org"

# input table should have phylotypes as rows and samples as columns

import argparse
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import math
from qiime2 import Artifact

## Input arguments
parser = argparse.ArgumentParser(
    description="run rank sums tests on case-control dataset"
)
parser.add_argument(
    "-i",
    help="input OTU table qiime artifact (rows = samples, "
    + " columns = phylotypes; default format = tab-delimited)",
    required=True,
)
parser.add_argument(
    "-m",
    help='case-control metadata with "disease_state" column',
    required=True,
)
parser.add_argument(
    "-o",
    help="output file name [default: %(default)s]",
    default="rank_sums_results.txt",
)
parser.add_argument("-a", help="alpha-level for test", default=0.05)
parser.add_argument(
    "-t", help="occurence threshold in case or control", default=0.3
)


args = parser.parse_args()

# Passing through \n doesn't work...
seps = {"tab": "\t", "newline": "\n", "comma": ","}

# load abundance matrix
art = Artifact.load(args.i)
df = art.view(pd.DataFrame).transpose()

# load metadata

meta = pd.read_csv(args.m, sep="\t", index_col=0).loc[df.columns]
case_samples = meta.index[meta["disease_state"] == "case"].tolist()
control_samples = meta.index[meta["disease_state"] == "control"].tolist()

# filter abundance table
df_case = df[case_samples]
df_control = df[control_samples]

sig_otus_all_data = []
all_pvals_data = []
sig_otus_all_data_names = []
all_pvals_data_names = []

# test for significant differences
for i in range(df_case.shape[0]):
    if df_control.iloc[i, :].astype(bool).sum() / float(
        df_control.shape[1]
    ) >= float(args.t) or df_case.iloc[i, :].astype(bool).sum() / float(
        df_case.shape[1]
    ) >= float(
        args.t
    ):
        all_pvals_data.append(
            sp.stats.ranksums(df_case.iloc[i, :], df_control.iloc[i, :])[1]
        )
        all_pvals_data_names.append([df_control.index[i], df_case.index[i]])
    else:
        all_pvals_data.append(np.nan)
        all_pvals_data_names.append([df_control.index[i], df_case.index[i]])


all_pvals_data = pd.Series(all_pvals_data, index=df_case.index)
all_pvals_data_nonan = all_pvals_data.dropna()

for i in range(len(all_pvals_data)):
    if all_pvals_data[i] <= float(args.a):
        sig_otus_all_data.append([all_pvals_data_names[i], all_pvals_data[i]])

pd.DataFrame(sig_otus_all_data).to_csv(args.o, sep="\t")
plt.hist(pd.Series(all_pvals_data).dropna())
plt.xlabel("p-value")
plt.ylabel("frequency")
plt.savefig("p-value_histogram.png", dpi=300)
