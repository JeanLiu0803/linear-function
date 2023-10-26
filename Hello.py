# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import numpy as np
from numpy.linalg import inv
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Linear function Maker",
        page_icon="🪄",
        initial_sidebar_state="collapsed",
    )

    st.write("# Welcome to linear function Maker! 👋")

    point1 = st.text_input("Please input first point (format: x1, y1)")
    point2 = st.text_input("Please input second point (format: x2, y2)")

    runbutton = st.button("Magic! 🪄")

    st.write("## Your function")
    if runbutton:
        if point1 != "" and point2 != "":
            [x1, y1] = point1.split(",")
            [x2, y2] = point2.split(",")
        # print(x1, y1)
        # print(x2, y2)

            m, b = line_formula(float(x1), float(y1), float(x2), float(y2))

            st.write("y = {}x + ({})".format(m, b))
    


def line_formula(x1, y1, x2, y2):
    x_array = np.array([[x1, 1],
                        [x2, 1]])
    y_array = np.array([[y1],
                        [y2]])
    
    x_inv = inv(x_array)
    ans = np.dot(x_inv, y_array)
    
    m = np.round(ans[0][0], 4)
    b = np.round(ans[1][0], 4)

    print('y = {}x + ({})'.format(m, b))

    return m, b

if __name__ == "__main__":
    run()
