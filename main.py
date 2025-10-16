#!/usr/bin/env python3
"""
Main script to load data and run validations.
"""

import json
from src.data_loader import load_data
from src.validations import run_validations

def main():
    print("Loading data...")
    data = load_data('data/sample_data.json')
    
    print("Running validations...")
    results = run_validations(data)
    
    print("Validation results:")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
