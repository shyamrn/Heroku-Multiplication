# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 12:32:54 2022

@author: SHYAM
"""

import streamlit as st

def main():
    st.title("Multiplication of Two Numbers")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">
    App for Multiplying Two Numbers </h2>
    </div>
    """    
    st.markdown(html_temp, unsafe_allow_html=True) 
    
    num_1 = st.text_input("Input the first number")
    num_2 = st.text_input("Input the second number")
    
        
    if st.button("Multiply"):
        
        try:
            Output = float(num_1) * float(num_2)
        
        except:
            Output = 'Invalid input'      
                
    st.success('Output: ' + str(Output))
    
    
if __name__ == '__main__':
    main()