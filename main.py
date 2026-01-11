import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = None
        self.load_dataset()
        self.check_dataset()

    def load_dataset(self):
        try:
            self.df = pd.read_csv(self.dataset_path)
            print("Dataset Sucessfully Loaded")
        except Exception as e:
            self.df = None
            print("Error loading dataset, " + str(e))

    def check_dataset(self):
        print("Dataset Check...")
        print(f"---Head: \n{self.df.head()}")
        print(f"---Info \n{self.df.info()}")
        print(f"---Shape: \n{self.df.shape}")
        print(f"---Columns: \n{self.df.columns}")
        print(f"---Nulls: \n{self.df.isnull().sum()}")

    def plot_prices(self):
        plt.figure(figsize=(10, 6))
        avg_prices = self.df.groupby('Brand')['Price_USD'].mean().sort_values()
        avg_prices.plot(kind='bar', color='steelblue', edgecolor='black')
        plt.xlabel('Avg Price (USD)', fontsize=12)
        plt.title('Brand Prices', fontsize=14)
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def populate_dataset(df):
        df['Car_Age'] = 2026 - df['Model_Year']
        df['Price_Per_Year'] = df['Price_USD'] / df['Car_Age']
        df['Price_Per_HP'] = df['Price_USD'] / df['Max_Power_bhp']
        df['Power_Per_Liter'] = df['Max_Power_bhp'] / (df['Engine_CC'] / 1000)
        df['Km_Per_Year'] = df['Kilometers_Driven'] / df['Car_Age']
        return df

    @staticmethod
    def draw_correlation_plot(df, group_by):
        cdf = df.drop(columns=["Car_ID"])
        cdf["Transmission"], mapping = pd.factorize(cdf["Transmission"])

        for item, group in cdf.groupby(group_by):
            corr = group.select_dtypes(include="number").corr()
            # corr = corr.where(abs(corr) >= 0.1)
            plt.figure(figsize=(8, 6))
            sns.heatmap(
                corr,
                annot=True,
                cmap="coolwarm",
                center=0,
                fmt=".2f"
            )
            plt.title(f"Correlation for {item}")
            plt.show()

    def analyze(self):
        if self.df is None:
            print("Dataset not loaded")
            return
        tdf = self.df.copy()
        tdf = self.populate_dataset(tdf)
        self.plot_prices()
        self.draw_correlation_plot(tdf, "Brand")

car_analyzer = DataAnalyzer("cars.csv")
car_analyzer.analyze()


