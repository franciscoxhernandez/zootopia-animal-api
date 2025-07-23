# 🦊 Zootopia-animal-api
This project fetches animal data from the [API Ninjas Animals API](https://api-ninjas.com/api/animals) and generates a simple, styled HTML website showing key information about a specific animal (e.g. diet, habitat, classification, etc.).
It’s built in Python with a modular architecture, separating the data-fetching logic from the website-generation logic.
You NEED an account in API Ninjas and create for your own API KEY


## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone git@github.com:yourusername/zootopia-animal-api.git
cd zootopia-animal-api
```
### 2. Install dependencies
```bash
pip install python-dotenv
```
### 3. Set your API KEY
```bash
API_KEY='your_actual_api_key_here'
```
### 4. Run the program
```bash
python animals_web_generator.py
```
You’ll be prompted to enter an animal name (e.g. Fox), and the script will:
	•	fetch the data from the API
	•	generate animals.html
	•	open it in your browser (or you can open it manually)

### 🧼 Notes

1. .env are excluded from Git using .gitignore
2.  generated file animals.html can be freely updated or opened in any browser 
3. You can easily extend the system to support other data sources or build a Flask web interface
