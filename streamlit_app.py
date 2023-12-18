import streamlit as st
import pandas as pd

def main():

	st.header('Canada/US Gas Price Comparison')
	st.subheader('Compare gas prices including currency exchange')
	
	c2u = 1.37
	u2c = round(1/c2u, 2)

	cdn = st.toggle("Canadian Dollars")

	amount = st.number_input("Enter Amount")
	
	if cdn:
		sCurrency, tCurrency = "Canadian", "American"
		sUnits, tUnits = "Litres", "gallons"
		st.write(f"Today's Exchange rate is \$CDN {c2u} = \$US 1.00")
		price = st.number_input("Enter gas price in \$CDN")
	else:
		sCurrency, tCurrency = "American", "Canadian"
		sUnits, tUnits = "gallons", "Litres"
		st.write(f"Today's Exchange rate is \$CDN 1.00 = \$US {u2c}")
		price = st.number_input("Enter gas price in \$US")

	convert = amount * price

	st.write(f"{amount} {sUnits} at {c2u} {sCurrency} dollars would cost {convert} {tUnits} {tCurrency}")

if __name__ == '__main__':
	main()	
