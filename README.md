
# 🧪 Toxicity Predictor — Pharmacogenomics Web App

This web app predicts the toxicity potential of SNP (single nucleotide polymorphism) and drug combinations using a machine learning model.

## 🚀 Live Demo

👉 [Click here to try the app](https://toxicity-predictor-quzgfex6vsmkrbczx26tbd.streamlit.app/)

## 🧠 How It Works

- Input your genetic variant (SNP) and drug data manually or upload a CSV file.
- The app uses a trained XGBoost model to predict whether the combination might lead to **toxic side effects**.
- A confidence score and additional variant details are displayed.

## 💡 Use Cases

- Personalized medicine decision-making
- Pharmacogenomics research
- Education/demonstration of SNP-drug interactions

## 🔧 Tech Stack

- Python 3.9
- Streamlit
- XGBoost
- Scikit-learn
- Pandas, NumPy
- Git LFS (for model storage)

## 📁 Files

| File                | Description                         |
|---------------------|-------------------------------------|
| `app.py`            | Main Streamlit app                  |
| `toxicity_model.pkl`| Trained ML model (XGBoost)          |
| `encoder.pkl`       | Encoded label mappings              |
| `test_input.csv`    | Sample input file for batch testing |

## 🛠️ Setup Instructions

1. Clone the repo  
   `git clone https://github.com/Abithaselvam/toxicity-predictor.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the app locally  
   `streamlit run app.py`

> For large model files, Git LFS is used.



## ✨ Future Improvements

- SNP pattern matching from genomic reports
- API version for integration
- Side-effect severity scoring

---

Made with ❤️ by Abitha Selvam
