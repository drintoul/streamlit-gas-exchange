import streamlit as st
import pandas as pd

def main():

	st.header('Canada/US Gas Price Comparison')
	st.subheader('Compare gas prices including currency exchange')
	
	c2u = 1.37
	u2c = round(1/c2u, 2)

	st.write(c2u, u2c)
	
	if cdn:
		st.write(f"Today's Exchange rate is \$CDN {c2u} = \$US 1.00")
		price = st.number_input("Enter today's gas price in \$CDN")
	else:
		st.write(f"Today's Exchange rate is \$CDN 1.00 = \$US {u2c}")
		price = st.number_input("Enter today's gas price in \$US")

	st.write(price)

if __name__ == '__main__':
	main()	
