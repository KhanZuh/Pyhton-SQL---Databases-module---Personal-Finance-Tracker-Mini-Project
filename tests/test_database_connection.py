# tests/test_database_connection.py

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data - note the correct path
    db_connection.seed("seeds/database_connection.sql")  # This should work from project root

    # Insert a new record
    db_connection.execute("INSERT INTO test_table (name) VALUES (%s)", ["second_record"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM test_table")

    # Assert that the results are what we expect
    assert result == [
        (1, "first_record"),
        (2, "second_record")
    ]

def test_database_connection_with_params(db_connection):
    # Seed the database
    db_connection.seed("seeds/database_connection.sql")
    
    # Test parameterized queries
    result = db_connection.execute("SELECT * FROM test_table WHERE name = %s", ["first_record"])
    
    assert result == [(1, "first_record")]