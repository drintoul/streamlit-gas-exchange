import streamlit as st
import pandas as pd

st.header('Canada/US Gas Price Comparison')
st.subheader('Compare gas prices including currency exchange')

dfs = pd.read_html("https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates")
df = dfs[0]
df = df[df['Currency'] == 'US dollar']

usd2cdn = df.iloc[-1, -1]
cdn2usd = round(1 / usd2cdn, 4)

col1, col2 = st.columns(2)
df.columns = df.iloc[0]
df = df[1:]
col1.dataframe(df.head(), hide_index=True)
#df2 = df.T
col2.dataframe(df, hide_index=True)
col2.line_chart(df)

cdn = st.toggle("Start with Canadian Dollars")

def main():

	if cdn:
		rate = cdn2usd
		st.write(f"Current Exchange Rate is \$CDN {rate} = \$USD 1.00")
		amount = st.number_input("Enter Amount of gas in Litres", value=5.0)
		sCurrency, tCurrency = "Canadian", "American"
		sUnits, tUnits = "Litre", "gallon"
		price = st.number_input("Enter gas price in \$CDN", value=1.15)
	else:
		rate = usd2cdn
		st.write(f"Current Exchange Rate is \$CDN 1.00 = \$USD {rate}")
		amount = st.number_input("Enter Amount of gas in gallons", value=5.0)
		sCurrency, tCurrency = "American", "Canadian"
		sUnits, tUnits = "gallon", "Litre"
		price = st.number_input("Enter gas price in \$US", value=3.0)

	cost =  price * amount / rate

	st.info(f"{amount} {sUnits}s at \${price:.2f}/{sUnits} with exchange rate of \${rate:.2f} would cost \${cost:.2f} {tCurrency}")

if __name__ == '__main__':
	main()	
