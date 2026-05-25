# HVAC Telemetry Anomaly Detection Pipeline

**Author:** Roneilfred O. Saad  
**Institution:** Technological University of the Philippines, Manila (TUP-M)  
**Course:** Computer Programming  

## 📌 Project Overview
This project is an automated, Object-Oriented Python data pipeline designed to ingest, clean, and analyze high-frequency HVAC (Heating, Ventilation, and Air Conditioning) telemetry. Specifically, the software is engineered to detect operational anomalies—such as severe aerodynamic pressure drops and duct leakage—by calculating the statistical variance of mechanical power draw and its correlation to supply temperatures. 

The pipeline transitions raw, noisy sensor logs into clean data arrays and generates both static and animated visualizations to highlight mechanical stress over time.

## ⚙️ System Architecture & Technologies Used
* **Language:** Python 3
* **Data Ingestion & Cleaning:** `pandas` (Used for programmatic filtering, handling NaN values, and type-casting).
* **Statistical Analytics:** `numpy` (Used for high-performance, C-optimized array calculations including Mean, Median, Variance, Standard Deviation, and Pearson Correlation).
* **Visualization Suite:** `matplotlib` and `seaborn` (Used to render histograms, boxplots, scatter plots, and temporal `.gif` animations).

## 📂 Repository Structure
* `main.py` - The core Object-Oriented Python script containing the `HVACAnomalyPipeline` class.
* `requirements.txt` - A list of all required Python libraries to run the script.
* `data/` - Contains the raw (`original.csv`) and cleaned (`dataset_cleaned.csv`) HVAC telemetry datasets.
* `outputs/` - Contains all generated outputs, including static graphs (`.png`), temporal animations (`.gif`), and the statistical results text file.
* `Saad_250679_IEEE_Paper.pdf` - The final IEEE-formatted research paper detailing the mathematical framework and engineering discussion of the findings.

## 🚀 How to Run the Pipeline

**1. Install Dependencies** Before running the script, ensure you have the required libraries installed. You can install them via the terminal or command prompt using:
```bash
pip install -r requirements.txt
