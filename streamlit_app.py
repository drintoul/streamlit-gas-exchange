import streamlit as st
import pandas as pd

def main():

	st.header('Canada/US Gas Price Comparison')
	st.subheader('Compare gas prices including currency exchange')

	dfs = pd.read_html("https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates")
	df = dfs[0]
	df = df[df['Currency'] == 'US dollar']
	st.dataframe(df.head(), hide_index=True)
	
	usd = df.iloc[-1, -1]
	can = round(1/c2u, 2)

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

	st.write(f"{amount} {sUnits} at {can} {sCurrency} dollars would cost {convert} {tUnits} {tCurrency}")

if __name__ == '__main__':
	main()	
