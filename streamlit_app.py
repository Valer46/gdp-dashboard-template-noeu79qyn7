import streamlit as st
import sys
import warnings
import matplotlib.pyplot as plt
from datetime import datetime

# Append your custom utility path
sys.path.append('./dtsUtility')

# Import your custom utility module
import dtsUtility
from dtsUtility.dts_main import DtsMonitoringSystem

# Suppress warnings
warnings.filterwarnings('ignore')

# Streamlit app
st.set_page_config(layout="wide")
st.title("DTS Monitoring System")

# Streamlit widgets for user input
well_names = ['SI14-N6', 'Other Well Names']  # Replace with your actual well names
well_name = st.selectbox('Select Well Name', well_names)

start_date = st.date_input('Start Date', datetime(2023, 1, 1))
end_date = st.date_input('End Date', datetime(2023, 1, 11))
interpolate_temp_data = st.checkbox('Interpolate Temp Data', True)
save_heatmap = st.checkbox('Save Heatmap', False)
user = st.text_input('User Prefix', 'nouser')

# Button to trigger the DTS system and plot
if st.button('Generate Heatmap'):
    start_date_str = start_date.strftime('%Y-%m-%d 00:00:00')
    end_date_str = end_date.strftime('%Y-%m-%d 00:00:00')
    
    dts_sys = DtsMonitoringSystem(well_name, times=[start_date_str, end_date_str], interpolate=interpolate_temp_data)
    
    fig, ax = plt.subplots(figsize=(9, 9))
    dts_sys.plot_heatmap(ax=ax, save=save_heatmap, prefix=user)
    
    st.pyplot(fig)
