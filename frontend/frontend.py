import streamlit as st
import requests

def main():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1531497865144-0464ef8fb9a9?auto=format&fit=crop&w=1350&q=80");
            background-size: cover;
            background-position: center;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: cyan;
            text-shadow: 1px 1px 2px black;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='title'>🕵️ Fake Company Detector</h1>", unsafe_allow_html=True)

    company_name = st.text_input('Enter Company Name 🖥️')

    registered = st.radio('Registered or not ®️', ('yes', 'NO'))
    company_age = st.number_input('Company Age', min_value=0, max_value=100, value=10, step=1)
    valid_address = st.radio('Is the address valid? 🛣️', ('yes', 'NO'))
    domain_age = st.number_input('Domain Age', min_value=0, max_value=100, value=10, step=1)
    listed_in_gov_db = st.radio('Listed on Gov site? ®️', ('yes', 'NO'))
    has_audited_reports = st.radio('Has Audited Reports 🔉', ('yes', 'NO'))

    def convert(value):
        return 1 if value.lower() == 'yes' else 0

    if st.button("🚀 Predict Fraud"):
        data = {
            "registered": convert(registered),
            "company_age": company_age,
            "valid_address": convert(valid_address),
            "domain_age": domain_age,
            "listed_in_gov_db": convert(listed_in_gov_db),
            "has_audited_reports": convert(has_audited_reports)
        }
        print(data)
    with st.spinner("🔍 Analyzing company details..."):
        try:
            res = requests.post("http://localhost:5000/predict", json=data)
            if res.status_code == 200:
                result = res.json()
                st.success(f"🧠 Prediction: {'Fraudulent' if result['prediction'] == 'fake' else 'Legit'}")

                

            else:
                st.error(f"❌ Backend Error: {res.text}")
        except Exception as e:
            st.error(f"connecting to backend.....: {e}")

if __name__ == '__main__':
    main()
