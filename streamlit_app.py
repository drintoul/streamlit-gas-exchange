import streamlit as st
import pandas as pd

def main():

	st.header('Canada/US Gas Price Comparison')
	st.subheader('Compare gas prices including currency exchange')
	
	exchange = 1.37

	cdn = st.toggle('Canadian Dollars')

	if cdn:
		st.write("Today's Exchange rate is $CDN {exchange} = $US 1.00")
	else:
		st.write("Today's Exchange rate is $CDN 1.00 == $US {1/exchange:1.2f}")

if __name__ == '__main__':
	main()	
