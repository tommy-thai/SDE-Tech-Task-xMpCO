# This is the main script where you will orchestrate the ETL process, feel free to completely modify the files/structure as you see fit.
import api_client
import transform_data
import load_to_database

if __name__ == "__main__":
    print("ETL Job Started")

    # Extract phase
    # TODO: Implement data extraction logic
    print("Extracting data from JSONPlaceholder API...")
    posts_data = api_client.get_posts()
    users_data = api_client.get_users()
    print("Extraction completed.")

    # Transform phase
    # TODO: Implement data transformation logic
    print("Transforming data...")
    transformed_posts = transform_data.parse_embedded_json(posts_data)
    transformed_posts = transform_data.add_computed_status(transformed_posts)
    enriched_posts = transform_data.combine_posts_with_users(transformed_posts, users_data)
    print("Transformation completed.")

    # Load phase
    # TODO: Implement data loading logic
    print("Loading data into the database...")
    conn, cursor = load_to_database.connect_to_database('etl_pipeline')
    load_to_database.create_table(cursor)
    load_to_database.load_data_into_table(cursor, enriched_posts)
    conn.commit()
    conn.close()
    print("Loading completed.")

    print("ETL Job Finished")
