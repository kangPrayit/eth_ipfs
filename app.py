import streamlit as st
import pandas as pd
from utils import get_data_from_contracts, upload_file_to_ipfs, simpan_data_to_smart_contract

st.title('Demo of Intelligent Manufacturing System')

with st.form(key='form1'):
    sid = st.text_input('sid')
    system_information = st.text_input('system_information')
    system_create = st.date_input('system_create')
    mid = st.text_input('module_manufacture_id')
    manufacture_date = st.date_input('module_manufacture_date')
    manufacture_id = st.text_input('ic_manufacturer_id')
    file = st.file_uploader('Upload File')
    submitted = st.form_submit_button('Save')

# Get data from smart contract
df = get_data_from_contracts()

# Jika tombol save ditekan
if submitted:
    if file is not None:
        ipfs_file_cid, filename = upload_file_to_ipfs(file)
    else:
        ipfs_file_cid = ""
        filename = ""

    # st.text(str(system_create))

    simpan_data_to_smart_contract(
        sid,
        system_information,
        str(system_create),
        mid,
        manufacture_id,
        str(manufacture_date),
        filename,
        ipfs_file_cid
    )
    # Refresh Data
    df = get_data_from_contracts()

st.subheader('Data')
st.table(df)