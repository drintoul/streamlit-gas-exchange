import streamlit as st
import pandas as pd

st.set_page_config(page_title="Canada/US Gas Price Comparison")
st.title('Canada/US Gas Price Comparison')
st.subheader('Calculate gas prices including currency exchange')

@st.cache_data(ttl=86400)
def fetch_exchange_rate():

	dfs = pd.read_html("https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates")
	df = dfs[0]
	df = df[df['Currency'] == 'US dollar']
	return df

df = fetch_exchange_rate()

usd2cdn = df.iloc[-1, -1]
cdn2usd = round(1 / usd2cdn, 4)

st.write("""Exchange Rate from Bank of Canada:
https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates""")

st.dataframe(df, hide_index=True)

#dfT = df.T
#dfT.columns = dfT.iloc[0]

#col1, col2 = st.columns(2)

#col1.dataframe(dfT[1:6])
#c = (alt.chart(dfT[1:6])
#     .mark_circle()
#)
#col2.altair_chart(c, use_container_width=True)

cdn = st.toggle("Start with Canadian Dollars", value=True)

def main():

	if cdn:
		rate = cdn2usd * 3.78541
		st.write(f"Current Exchange Rate is \$CDN {rate} = \$USD 1.00")
		#amount = st.number_input("Enter Amount of gas in Litres", value=5.0)
		amount = st.slider("Enter Amount of gas in Litres", 1.0, 40.0, 10.0, step=0.1, format="%f")
		sCurrency, tCurrency = "Canadian", "American"
		sUnits, tUnits = "Litre", "gallon"
		#price = st.number_input("Enter gas price in \$CDN", value=1.15)
		price = st.slider("Enter gas price in \$CDN", 0.7, 2.0, 1.15, step=0.01, format="%f")
	else:
		rate = usd2cdn / 3.78541
		st.write(f"Current Exchange Rate is \$CDN 1.00 = \$USD {rate}")
		#amount = st.number_input("Enter Amount of gas in gallons", value=5.0)
		amount = st.slider("Enter Amount of gas in gallons", 1.0, 15.0, 10.0, step=0.1, format="%f")
		sCurrency, tCurrency = "American", "Canadian"
		sUnits, tUnits = "gallon", "Litre"
		#price = st.number_input("Enter gas price in \$US", value=3.0)
		price = st.slider("Enter gas price in \$USD", 2.0, 5.0, 3.0, step=0.01, format="%f")
		
	cost =  price * amount * rate

	st.info(f"{amount} {sUnits}s at \${price:.2f}/{sUnits} {sCurrency} with an exchange rate of \${rate:.2f} would cost \${cost:.2f} {tCurrency}", icon="💰")

if __name__ == '__main__':
	main()	
