import streamlit as st
import pandas as pd

def main():

  dfs = pd.read_hmtl('https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/')
  #df = dfs[0]
  st.write(dfs)
  #st.dataframe(df)

if __name__ == '__main__':
	main()	
