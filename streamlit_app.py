import streamlit as st
import pandas as pd

def main():

  #dfs = pd.read_html('https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/')
  #df = dfs[0]
  #st.write(dfs)
  #st.dataframe(df)

  cdn = st.toggle('Canadian Dollars')

  if cdn:
     	st.write('Canadian Dollars')
  else:
	st.write('U.S. Dollars')

if __name__ == '__main__':
	main()	
