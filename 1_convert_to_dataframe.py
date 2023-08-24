# starting with the bibtex files from WoS, we utilize the Bibliometrix biblioshiny app to convert the bibtex files to a dataframe in R
# documentation for that is here --> https://www.bibliometrix.org/home/index.php/layout/biblioshiny
# this script takes the resulting Rdata file and converts it into a dataframe in python

# import packages
import pandas as pd
import pyreadr
import pickle

# read in the Rdata file
result = pyreadr.read_r("peds_spine.RData")

# the dataframe is the first (and only) object in the result
R_df = next(iter(result.keys()))
df = result[R_df]  # extract R dataframe into pandas

# clean up the dataframe
df = df.reset_index().drop(columns="rownames")
df["PY"] = df["PY"].astype(int) # convert publication year to integer

# save the dataframe as a csv for inspection
df.to_csv("peds_spine_v1_from_R.csv", index=False)

# save the dataframe as a pickle to preserve the data types
with open("peds_spine_v1_from_R.pkl", "wb") as f:
    pickle.dump(df, f)