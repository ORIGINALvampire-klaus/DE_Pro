def transform_data(data):
    if data is not None:

        data_filtered = data[data['TotalOrders'] < 30]  # Adjust column name as needed
        # Add a new column "Discount" based on total orders
        data_filtered['Discount'] = data_filtered['TotalOrders'].apply(lambda x: 0.1 if x > 50 else 0.05)
        print("Data transformed successfully")
        return data_filtered
    else:
        print("No data to transform")
        return None