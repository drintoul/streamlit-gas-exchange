import streamlit as st
import pandas as pd

def main():

	st.header('Canada/US Gas Price Comparison')
	st.subheader('Compare gas prices including currency exchange')

	dfs = pd.read_html("https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates")
	df = dfs[0]
	df = df[df['Currency'] == 'US dollar']
	st.dataframe(df.head(), hide_index=True)
	
	usd2can = df.iloc[-1, -1]
	can2usd = round(1/usd2can, 2)

	cdn = st.toggle("Start with Canadian Dollars")
	
	if cdn:
		st.write(f"Today's Exchange rate is \$CDN {can2usd} = \$US 1.00")
		amount = st.number_input("Enter Amount of gas in Litres", value=1.15, min_value=0.5, max_value=3)
		sCurrency, tCurrency = "Canadian", "American"
		sUnits, tUnits = "Litres", "gallons"
		price = st.number_input("Enter gas price in \$CDN")
	else:
		st.write(f"Today's Exchange rate is \$CDN 1.00 = \$US {usd2can}")
		amount = st.number_input("Enter Amount of gas in gallons", value=3, min_value=1, max_value=5)
		sCurrency, tCurrency = "American", "Canadian"
		sUnits, tUnits = "gallons", "Litres"
		price = st.number_input("Enter gas price in \$US")

	convert = round(amount * price, 2)

	st.write(f"{amount} {sUnits} at {price} {sUnits} would cost {convert} {tCurrency} dollars")

if __name__ == '__main__':
	main()	
