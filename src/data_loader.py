import pandas as pd

def load_all_data(base_path="../data/raw/"):
    customers = pd.read_csv(base_path + "customers.csv")
    loans = pd.read_csv(base_path + "loans.csv")
    applications = pd.read_csv(base_path + "applications.csv")
    transactions = pd.read_csv(base_path + "transactions.csv")
    defaults = pd.read_csv(base_path + "defaults.csv")
    branches = pd.read_csv(base_path + "branches.csv")

    return customers, loans, applications, transactions, defaults, branches
