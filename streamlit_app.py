import streamlit as st
import pandas as pd

st.header('Canada/US Gas Price Comparison')
st.subheader('Compare gas prices including currency exchange')

dfs = pd.read_html("https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates")
df = dfs[0]
df = df[df['Currency'] == 'US dollar']
st.dataframe(df.head(), hide_index=True)
	
usd2cdn = df.iloc[-1, -1]
cdn2usd = round(1 / usd2cdn, 4)

cdn = st.toggle("Start with Canadian Dollars")

def main():

	if cdn:
		rate = cdn2usd
		st.write(f"Today's Exchange rate is \$CDN {cdn2usd} = \$US 1.00")
		amount = st.number_input("Enter Amount of gas in Litres", value=5.0)
		sCurrency, tCurrency = "Canadian", "American"
		sUnits, tUnits = "Litre", "gallon"
		price = st.number_input("Enter gas price in \$CDN", value=1.15)
	else:
		rate = usd2cdn
		st.write(f"Today's Exchange rate is \$CDN 1.00 = \$US {usd2cdn}")
		amount = st.number_input("Enter Amount of gas in gallons", value=5.0)
		sCurrency, tCurrency = "American", "Canadian"
		sUnits, tUnits = "gallon", "Litre"
		price = st.number_input("Enter gas price in \$US", value=3.0)

	cost = round(amount * rate, 2)

	st.write(f"{amount} {sUnits}s at \${round(price, 2)}/{sUnits} would cost \${round(cost, 2)} {tCurrency} dollars")

if __name__ == '__main__':
	main()	
