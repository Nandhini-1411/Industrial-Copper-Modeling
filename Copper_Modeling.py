import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
item_type_encoded = {'IPL': 0, 'Others': 1, 'PL': 2, 'S': 3, 'SLAWR': 4, 'W': 5, 'WI': 6}
status_encoded = {'Draft': 0,'Lost': 1,'Not lost for AM': 2,'Offerable': 3,'Offered': 4,'Revised': 5,
                  'To be approved': 6, 'Won': 7, 'Wonderful': 8}

def predict_status(country,item_type,order_day,order_month,order_year,delivery_year,delivery_month,delivery_day,
                    application, width, product_ref,thickness_boxcox, quantity_tons_boxcox, selling_price):
    item_type_encoded_value = item_type_encoded[item_type]
    order_day = item_date_input.day
    order_month = item_date_input.month
    order_year = item_date_input.year
    with open(r"D:\CAPSTONE\COPPER\Classification_Model.pkl", "rb") as f:
        model_class = pickle.load(f)
    user_data = np.array([[country,item_type_encoded_value, order_year, order_month, order_day, delivery_year, 
                            delivery_month, delivery_day, application, width, product_ref, thickness_boxcox, 
                            quantity_tons_boxcox, selling_price]])
    y_pred = model_class.predict(user_data)
    return y_pred[0]
    
def predict_selling_price(country, status, item_type, item_date_input, delivery_year,delivery_month,delivery_day, 
                          application, width, product_ref,thickness_boxcox, quantity_tons_boxcox):
    status_encoded_value = status_encoded[status]
    item_type_encoded_value = item_type_encoded[item_type]
    order_day = item_date_input.day
    order_month = item_date_input.month
    order_year = item_date_input.year
    with open(r"D:/CAPSTONE/COPPER/Regression_Model.pkl", "rb") as f:
        model_regg = pickle.load(f)
    user_data = np.array([[country, status_encoded_value, item_type_encoded_value, order_year, order_month,
                            order_day, delivery_year, delivery_month, delivery_day, application, width,
                              product_ref, thickness_boxcox, quantity_tons_boxcox]])
    y_pred = model_regg.predict(user_data)
    return y_pred[0]

st.set_page_config(layout="wide")
st.title("**INDUSTRIAL COPPER MODELING**")
with st.sidebar:
    option = option_menu('Main Menu', options=["PREDICT SELLING PRICE", "PREDICT STATUS"])
if option == "PREDICT SELLING PRICE":
    st.header("PREDICT SELLING PRICE")
    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Enter Country", options=['25', '26', '27', '28', '30', '32', '38', '39', '40', '77', '78', '79', '80', '84', '89', '107', '113'])
        item_type = st.selectbox("Enter Item Type", options=list(item_type_encoded.keys()))
        status = st.selectbox("Enter Status", options=list(status_encoded.keys()))
        application = st.selectbox("Enter Application",options=["10.0", "41.0", "15.0", "59.0", "42.0", "56.0", "29.0", "26.0", "27.0", "28.0", "25.0", "40.0", "79.0",
                                                                    "22.0", "66.0", "20.0", "3.0", "38.0", "58.0", "65.0", "4.0", "68.0", "39.0", "67.0", "19.0", "99.0",
                                                                      "69.0", "5.0", "70.0", "2.0"])
        item_date_input = st.date_input('Select Order Date')
    with col2:
        width = st.number_input("Enter Width")
        thickness_boxcox = st.number_input("Enter Thickness")
        quantity_tons_boxcox = st.number_input("Enter Quantity in Tons")
        delivery_date_input = st.date_input('Select Delivery Date')
        product_ref = st.number_input("Enter Product Reference")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Predict Selling Price"):
            price = predict_selling_price(country, status, item_type, item_date_input, delivery_date_input.year,
                                          delivery_date_input.month, delivery_date_input.day, application, 
                                          width, product_ref, thickness_boxcox, quantity_tons_boxcox)
            st.success(f"**{price:.2f}**")
if option == "PREDICT STATUS":
    st.header("PREDICT STATUS (Won / Lose)")
    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Enter Country", options=['25', '26', '27', '28', '30', '32', '38', '39', '40', '77', '78', '79', '80', '84', '89', '107', '113'])
        item_type = st.selectbox("Enter Item Type", options=list(item_type_encoded.keys()))
        application = st.selectbox("Enter Application",options=["10.0", "41.0", "15.0", "59.0", "42.0", "56.0", "29.0", "26.0", "27.0", "28.0", "25.0", "40.0", "79.0",
                                                                    "22.0", "66.0", "20.0", "3.0", "38.0", "58.0", "65.0", "4.0", "68.0", "39.0", "67.0", "19.0", "99.0",
                                                                      "69.0", "5.0", "70.0", "2.0"])
        item_date_input = st.date_input('Select Order Date')
        selling_price = st.number_input("Enter Selling Price")
    with col2:
        width = st.number_input("Enter Width")
        thickness_boxcox = st.number_input("Enter Thickness")
        quantity_tons_boxcox = st.number_input("Enter Quantity in Tons")
        delivery_date_input = st.date_input('Select Delivery Date')
        product_ref = st.number_input("Enter Product Reference")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Predict Status"):
            status = predict_status(country, item_type, item_date_input.day, item_date_input.month, item_date_input.year, 
                delivery_date_input.year, delivery_date_input.month, delivery_date_input.day, 
                application, width, product_ref, thickness_boxcox, quantity_tons_boxcox, selling_price)
            if status == 1:
                st.success("**The Status is WON**")
            else:
                st.error("**The Status is LOST**")
