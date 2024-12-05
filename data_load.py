def load_data_to_csv(data, file_path="transformed_data.csv"):
    if data is not None:
        try:
            data.to_csv(file_path, index=False)
            print(f"Data loaded successfully to {file_path}")
        except Exception as e:
            print(f"Error loading data to CSV: {e}")
    else:
        print("No data to load.")
