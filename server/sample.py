from flask import Flask, jsonify
import psycopg2


app = Flask(__name__)

# Database connection parameters
db_host = 'database-work.c2bsg3plgld1.us-east-1.rds.amazonaws.com'
db_name = 'FYP'
db_user = 'postgres'
db_password = 'Matthias159!'

@app.route('/')
def get_data_from_db():
    try:
        # Connect to the AWS RDS PostgreSQL database
        connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Execute a SQL query to fetch data from a table (replace 'your_table_name' with your actual table name)
        cursor.execute('SELECT * FROM churn')

        # Fetch all rows from the query result
        data = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        # Convert the data to a list of dictionaries for JSON response
        result = []
        for row in data:
            result.append({
                'column1_name': row[0],
                'column2_name': row[1],
                # Add more columns as needed
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
