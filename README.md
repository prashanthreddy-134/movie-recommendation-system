# 🎬 Movie Recommendation System

A Python-based **content-based movie recommendation system** that recommends similar movies based on movie features.

The project includes an interactive **Streamlit web application** that allows users to select a movie and receive recommendations.

---

## 📌 Project Overview

The Movie Recommendation System analyzes movie information and calculates similarity between movies.

It uses a **content-based filtering** approach.

Unlike collaborative filtering, this system does not require ratings from other users. Instead, it recommends movies based on the characteristics of the selected movie.

### Recommendation Pipeline

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Feature Processing
      ↓
Similarity Calculation
      ↓
Find Similar Movies
      ↓
Display Recommendations
```

---

# 🚀 Features

- 🎬 Movie recommendations
- 🔎 Movie selection
- 🤖 Content-based filtering
- 📊 Similarity-based recommendations
- 🐍 Python implementation
- 🌐 Streamlit web application
- 📁 CSV-based movie dataset
- ⚡ Fast recommendations
- 💻 Interactive user interface
- 📦 Easy local installation

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and similarity |
| Streamlit | Web application |
| CSV | Dataset storage |

---

# 📂 Project Structure

```text
movie-recommendation-system/
│
├── data/
│   └── movies.csv
│
├── app.py
├── recommender.py
├── create_dataset.py
├── upgrade_project.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 💻 How to Run the Project

Follow these steps after downloading or cloning the repository.

## 1️⃣ Install Python

Install **Python 3.9 or newer**.

Check Python:

```bash
python --version
```

If `python` does not work on Windows:

```bash
py --version
```

---

## 2️⃣ Clone the Repository

Open PowerShell, Command Prompt, or Terminal:

```bash
git clone https://github.com/prashanthreddy-134/movie-recommendation-system.git
```

---

## 3️⃣ Enter the Project Folder

```bash
cd movie-recommendation-system
```

---

## 4️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

---

## 5️⃣ Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

---

## 6️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

You should see a URL similar to:

```text
Local URL: http://localhost:8501
```

Open this URL in your browser:

```text
http://localhost:8501
```

---

# ⚡ Quick Start

If Python is already installed and you don't want to create a virtual environment:

```bash
git clone https://github.com/prashanthreddy-134/movie-recommendation-system.git
cd movie-recommendation-system
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

# 🪟 Windows PowerShell — Complete Setup

Copy and run these commands **one at a time**:

```powershell
git clone https://github.com/prashanthreddy-134/movie-recommendation-system.git
```

```powershell
cd movie-recommendation-system
```

```powershell
python -m venv venv
```

```powershell
.\venv\Scripts\Activate.ps1
```

```powershell
python -m pip install -r requirements.txt
```

```powershell
python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

# 🖥️ How to Use the Application

After the application opens:

1. Select a movie.
2. The system analyzes the selected movie.
3. Movie features are processed.
4. Similarity between movies is calculated.
5. Similar movies are identified.
6. Recommendations are displayed.

---

# 🛑 Stop the Application

To stop Streamlit:

```text
Ctrl + C
```

---

# 🔄 Recreate the Dataset

The project includes a dataset creation script.

Run:

```bash
python create_dataset.py
```

---

# 🔧 Upgrade the Project

The repository also contains:

```text
upgrade_project.py
```

Run:

```bash
python upgrade_project.py
```

---

# 🧠 Recommendation Method

The system uses **content-based filtering**.

The recommendation engine compares movie characteristics and calculates similarity.

### Process

```text
User Selects Movie
        ↓
Movie Features Extracted
        ↓
Features Compared
        ↓
Similarity Calculated
        ↓
Similar Movies Sorted
        ↓
Recommendations Displayed
```

---

# 🎯 Example

A user selects a movie from the application.

The system analyzes the movie's available features and finds movies with similar characteristics.

The application then displays those movies as recommendations.

---

# 📊 Machine Learning Concepts Demonstrated

This project demonstrates:

- Python programming
- Data preprocessing
- Content-based filtering
- Feature processing
- Similarity calculation
- Machine learning
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- End-to-end ML application development

---

# 📦 Requirements

All dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
python -m pip install -r requirements.txt
```

---

# ❗ Troubleshooting

## Python is not recognized

Try:

```bash
py --version
```

Then:

```bash
py -m pip install -r requirements.txt
```

And:

```bash
py -m streamlit run app.py
```

---

## Streamlit is not recognized

Use:

```bash
python -m streamlit run app.py
```

instead of:

```bash
streamlit run app.py
```

---

## Port 8501 is already in use

Run:

```bash
python -m streamlit run app.py --server.port 8502
```

Then open:

```text
http://localhost:8502
```

---

## Dependency Installation Problem

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Then reinstall:

```bash
python -m pip install -r requirements.txt
```

---

# 🔮 Future Improvements

Possible improvements include:

- ⭐ User rating-based recommendations
- 👤 Personalized recommendations
- 🎭 Genre-based filtering
- 🔥 Trending movies
- 🎞️ Movie posters
- 🔍 Advanced movie search
- 🌐 Movie API integration
- 🧠 Hybrid recommendation system
- 📊 Recommendation analytics
- ☁️ Cloud deployment
- 📱 Mobile-friendly interface

---

# ⚠️ Limitations

The recommendation quality depends on the movie dataset and the features available in the dataset.

Because this is a content-based recommendation system, recommendations may not fully represent an individual's personal preferences.

Adding user ratings, watch history, and behavioral information could improve personalization.

---

# 👨‍💻 Author

## Prashanth Reddy S

**BE – Information Science & Engineering**

### Interests

- Machine Learning
- Artificial Intelligence
- Python
- Data Science
- Full-Stack Development
- Computer Vision

---

# 📜 License

This project is intended for educational and portfolio purposes.

---

# ⭐ GitHub Repository

https://github.com/prashanthreddy-134/movie-recommendation-system

If you find this project useful, consider giving the repository a ⭐.