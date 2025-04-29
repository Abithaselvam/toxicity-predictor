import streamlit as st
import pandas as pd
import joblib
model = joblib.load('toxicity_model.pkl')
encoder = joblib.load('encoder.pkl')

st.title("🧬 Toxicity Predictor")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Preview of Input Data")
    st.dataframe(df)

    # Encode categorical features
    encoded_input = encoder.transform(df)

    # Predict class and probabilities
    predictions = model.predict(encoded_input)
    probabilities = model.predict_proba(encoded_input)
    
    # Get labels and confidence
    toxicity_labels = ['Non-Toxic', 'Toxic']
    df['Toxicity_Prediction'] = [toxicity_labels[p] for p in predictions]
    df['Confidence_Score'] = (probabilities.max(axis=1) * 100).round(2).astype(str) + '%'

    # Add rule-based interpretation
    def get_explanation(pred):
        return "Potential adverse effect. Monitor closely." if pred == 1 else "Likely safe with current dosage."

    df['Interpretation'] = [get_explanation(p) for p in predictions]

    st.subheader("🔬 Predictions")
    st.dataframe(df)

    # Download button
    st.download_button("⬇️ Download Predictions", data=df.to_csv(index=False).encode('utf-8'),
                       file_name="toxicity_predictions.csv", mime="text/csv")

