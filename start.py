import os
import argparse
import pandas as pd
import streamlit as st
from config import DATA_PATH


# parse arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument("--local", action='store_true', help="If local data is taken from the local folder")
args = parser.parse_args()

# set page configuration
st.set_page_config("Model Monitoring")

# set headers
st.markdown("# Model Monitoring. " + ("Local" if args.local else "DB") + " data.")

st.markdown("## Welcome to the Start Page!")

# add radio buttons for selection which data would be used in the future
data_mode = st.radio("Please select data", ("Standard", "Upload from .csv"))

# add data upoading section
if data_mode == "Upload from .csv":
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.DataFrame()
else:
    df = pd.read_csv(os.path.join(DATA_PATH, "train.csv"), encoding="cp1252", 
                     usecols=['accommodates', 'bathrooms', 'bedrooms', 'beds', 
                              'latitude', 'longitude', 'review_scores_rating'])
    df.bathrooms = df.bathrooms.astype(int)
    df.bedrooms = df.bedrooms.astype(int)
    df.beds = df.beds.astype(int)
    df.review_scores_rating = df.review_scores_rating.astype(int)
    

# display uploaded file
if not df.empty:
    st.table(df.head(5).append(df.tail(5)))

# load data
# df_metrics = pd.read_csv(os.path.join(DATA_PATH, 'metrics.csv'))
# df_pr_rec = pd.read_csv(os.path.join(DATA_PATH, 'precision_recall.csv'))
# df_fp_tp = pd.read_csv(os.path.join(DATA_PATH, 'fpr_tpr.csv'))
# df_psi = pd.read_csv(os.path.join(DATA_PATH, 'psi.csv'))
