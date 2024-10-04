import time
import numpy as np
import streamlit as st

last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    # print(f"{i:2d}: {last_rows}")
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    chart.add_rows(new_rows)
    last_rows = new_rows
    time.sleep(0.05)



