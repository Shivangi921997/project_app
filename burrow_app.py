import streamlit as st
import numpy as np

st.title("Burrow Size Estimator")
age = st.number_input("Enter Age (in days):", min_value=10)

# Data
raw_ages = [10, 18, 18, 23, 25, 25, 28, 30, 33, 38, 43, 46, 60, 65, 72, 130, 160, 365]
raw_min = [0, 0, 0.35, 0.35, 0.5, 1, 2, 5, 8, 14, 35, 50, 70, 80, 100, 140, 175, 250]
raw_max = [0, 0, 0.5, 0.5, 1, 1.5, 3, 7, 10, 17, 45, 57, 75, 90, 120, 170, 200, 400]
raw_diam = [0, 0, 0.5, 0.5, 1, 1.5, 2, 2.5, 3, 3, 4, 4.5, 4.5, 4.5, 4.8, 7, 7.5, 9.4]

raw_ages = np.array(raw_ages)
raw_min = np.array(raw_min)
raw_max = np.array(raw_max)
raw_diam = np.array(raw_diam)

# Clean and average duplicate ages
unique_ages = np.unique(raw_ages)
avg_min = [np.mean(raw_min[raw_ages == a]) for a in unique_ages]
avg_max = [np.mean(raw_max[raw_ages == a]) for a in unique_ages]
avg_diam = [np.mean(raw_diam[raw_ages == a]) for a in unique_ages]

# Estimate
minLength_mm = np.interp(age, unique_ages, avg_min)
maxLength_mm = np.interp(age, unique_ages, avg_max)
diameter_mm  = np.interp(age, unique_ages, avg_diam)

# Convert to inches
minLength_in = minLength_mm / 25.4
maxLength_in = maxLength_mm / 25.4
diameter_in = diameter_mm / 25.4

# Output
st.markdown(f"**Length:** {minLength_mm:.2f}–{maxLength_mm:.2f} mm ({minLength_in:.2f}–{maxLength_in:.2f} in)")
st.markdown(f"**Diameter:** {diameter_mm:.2f} mm ({diameter_in:.2f} in)")
