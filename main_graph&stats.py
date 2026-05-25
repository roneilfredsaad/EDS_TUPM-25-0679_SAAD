import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time

class HVACAnomalyPipeline:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.cleaned_df = None
        
        # Ensure output directory exists
        if not os.path.exists("outputs"):
            os.makedirs("outputs")

    def ingest_and_filter_data(self):
        """Task 1: Load data and apply unique student filter"""
        try:
            print("1. Loading and filtering data...")
            self.df = pd.read_csv(self.file_path)
            
            # Using your exact column name: 'Timestamp'
            self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'], errors='coerce')
            
            # UNIQUE FILTER: Restrict data strictly to December
            self.df = self.df[self.df['Timestamp'].dt.month == 12]
            print(f"   -> Success! Filtered to {len(self.df)} rows for December.")
        except Exception as e:
            print(f"Ingestion Error: {e}")

    def clean_data(self):
        """Task 2: Automated cleaning"""
        try:
            print("2. Cleaning data and fixing types...")
            self.cleaned_df = self.df.drop_duplicates().dropna()
            
            # Using your exact column names: 'Power' and 'T_Supply'
            self.cleaned_df['Power'] = pd.to_numeric(self.cleaned_df['Power'], errors='coerce')
            self.cleaned_df['T_Supply'] = pd.to_numeric(self.cleaned_df['T_Supply'], errors='coerce')
            
            self.cleaned_df = self.cleaned_df.dropna()
            self.cleaned_df.to_csv("dataset_cleaned.csv", index=False)
            print("   -> Success! Cleaned dataset saved.")
        except Exception as e:
            print(f"Cleaning Error: {e}")

    def run_numpy_analytics(self):
        """Task 3: Engineering Analytics using NumPy"""
        try:
            print("3. Running NumPy statistics...")
            power_array = self.cleaned_df['Power'].values
            temp_array = self.cleaned_df['T_Supply'].values

            stats = {
                "Mean Power": np.mean(power_array),
                "Median Power": np.median(power_array),
                "Power Std Dev": np.std(power_array),
                "Power Variance": np.var(power_array)
            }
            r_value = np.corrcoef(temp_array, power_array)[0, 1]
            
            # SAVE RESULTS TO A TEXT FILE FOR YOUR IEEE PAPER
            with open("outputs/statistical_results.txt", "w") as f:
                f.write("--- STATISTICAL RESULTS (R. Saad / TUPM-25-0679) ---\n")
                for key, value in stats.items():
                    f.write(f"{key}: {value:.2f}\n")
                f.write(f"Pearson Correlation (r): {r_value:.3f}\n")
                f.write("--------------------------------------------------\n")
            print("   -> Success! Statistics saved to text file.")
                
        except Exception as e:
            print(f"Analytics Error: {e}")

    def generate_static_plots(self):
        """Task 4: Static Visualizations"""
        try:
            print("4. Generating engineering visualizations...")
            # 1. Histogram
            plt.figure(figsize=(8, 5))
            sns.histplot(self.cleaned_df['Power'], bins=30, kde=True, color='blue')
            plt.title("Distribution of HVAC Power (Dec)")
            plt.savefig("outputs/1_power_distribution.png")
            plt.close()

            # 2. Boxplot
            plt.figure(figsize=(8, 5))
            sns.boxplot(x=self.cleaned_df['Power'], color='cyan')
            plt.title("Outlier Detection in HVAC Power")
            plt.savefig("outputs/2_power_outliers.png")
            plt.close()

            # 3. Scatter Plot
            plt.figure(figsize=(8, 5))
            sns.scatterplot(x='T_Supply', y='Power', data=self.cleaned_df, alpha=0.5)
            plt.title("HVAC Power vs. Supply Temperature")
            plt.savefig("outputs/3_temp_vs_power_scatter.png")
            plt.close()
            print("   -> Success! Graphs saved to outputs folder.")
        except Exception as e:
            print(f"Plotting Error: {e}")

if __name__ == "__main__":
    print("=== HVAC TELEMETRY PIPELINE ===")
    
    hvac_pipeline = HVACAnomalyPipeline("hvac_telemetry.csv")
    hvac_pipeline.ingest_and_filter_data()
    
    if hvac_pipeline.df is not None:
        hvac_pipeline.clean_data()
        hvac_pipeline.run_numpy_analytics()
        hvac_pipeline.generate_static_plots()
        
    print("\nPIPELINE COMPLETE! Check the 'outputs' folder in your File Manager.")
    print("This screen will close in 10 seconds...")
    time.sleep(10)
