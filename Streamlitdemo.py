# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:18:29 2023

@author: Codelogic
"""
import streamlit as st
import pandas as pd 
import numpy as np
import plyer
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
#file=plyer.filechooser.open_file()
file="C:/Users/Codelogic/OneDrive - CODELOGICX TECHNOLOGIES PVT LTD/Desktop/Insurance/data/LFG-Pyle-Booth-M49-STD-100KS-INC-134K.CSV"
data=pd.read_csv(file).select_dtypes(include='number')
data.drop(data.filter(regex="Unname"),axis=1, inplace=True)
gb = GridOptionsBuilder.from_dataframe(data)
gb.configure_columns(data.columns,editable=True)
gb.configure_column('Year',editable=False)
gb.configure_column('Age',editable=False)
#gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
#gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_return = AgGrid(
    data,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='alpine', #Add theme color to the table
    enable_enterprise_modules=True,
    height=1000, 
    reload_data=False
)
if st.button("Submit"):
    df = grid_return['data']
    print(df)
    olddf=data.copy()
    newdf=df.copy()
    dep=[0,0,1,1,1,1,1,1,1,1]
    