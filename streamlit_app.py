import streamlit as st
import pandas as pd

st.set_page_config(page_title="Canada/US Gas Price Comparison")
st.title('Canada/US Gas Price Comparison')
st.subheader('Calculate gas prices including currency exchange')

def main():

	@st.cache_data(ttl=3600*6)
	def fetch_exchange_rate():

		dfs = pd.read_html("https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates")
		df = dfs[0]
		df = df[df['Currency'] == 'US dollar']
		asof = df.columns[-1]
		return df, asof

	df, asof = fetch_exchange_rate()

	cdn = st.toggle("Start with Canadian Dollars", value=True)

	usd2cdn = df.iloc[-1, -1]
	cdn2usd = round(1 / usd2cdn, 4)

	st.write("""Exchange Rate from Bank of Canada:
	https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates""")

	if cdn:
		rate = cdn2usd 
		st.write(f"As of {asof}: \$CDN 1.00 = \$USD {rate:.3f}")
		st.divider()
		#amount = st.number_input("Enter Amount of gas in Litres", value=5.0)
		amount = st.slider("Amount of gas in Litres", 1.0, 40.0, 10.0, step=0.1, format="%f")
		convert = amount / 3.78541
		sCurrency, tCurrency = "Canadian", "American"
		sUnits, tUnits = "Litre", "gallon"
		#price = st.number_input("Enter gas price in \$CDN", value=1.15)
		price = st.slider("Gas price in \$CDN", 0.5, 2.0, 1.15, step=0.01, format="%f")
	else:
		rate = usd2cdn # / 3.78541
		st.write(f"As of {asof}: \$CDN {rate:.3f} = \$USD 1.00")
		st.divider()
		#amount = st.number_input("Enter Amount of gas in gallons", value=5.0)
		amount = st.slider("Amount of gas in gallons", 1.0, 15.0, 10.0, step=0.1, format="%f")
		convert = amount * 3.78541
		sCurrency, tCurrency = "American", "Canadian"
		sUnits, tUnits = "gallon", "Litre"
		#price = st.number_input("Enter gas price in \$US", value=3.0)
		price = st.slider("Gas price in \$USD", 2.0, 5.0, 3.0, step=0.01, format="%f")
		
	cost =  price * amount * rate

	st.info(f"""{amount:.1f} {sUnits}s ({convert:.1f} {tUnits}s) at {sCurrency} \${price:.2f}/{sUnits} 
 		with an exchange rate of \${rate:.3f} {tCurrency} = \$1.00 {sCurrency} 
 		would cost \${cost:.2f} {tCurrency} (\${cost/rate:.2f} {sCurrency})""", icon="💰")

if __name__ == '__main__':
	main()	
