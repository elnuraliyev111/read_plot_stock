import streamlit as st
from multiapp import MultiApp
from apps import data, model, single_stock, spread # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App

This multi-page app is using the [streamlit-multiapps]
""")

# Add all your application here
app.add_app("Single Stock", single_stock.app)
#app.add_app("Data", data.app)
#app.add_app("Model", model.app)
app.add_app("Spread", spread.app)
# The main app
app.run()


