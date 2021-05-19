import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():

    a = st.number_input("Please input First Number")
    b = st.number_input("Please input Second Number")
    c = a+b
    st.text("The result of addition is")
    st.write(c)










