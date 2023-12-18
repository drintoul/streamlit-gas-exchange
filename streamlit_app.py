import streamlit as st
import pandas as pd

def main():

	exchange = 1.37

	cdn = st.toggle('Canadian Dollars')

	if cdn:
		st.write('Canadian Dollars')
	else:
		st.write('U.S. Dollars')

if __name__ == '__main__':
	main()	
