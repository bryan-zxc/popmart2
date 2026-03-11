"""Sample Customers.csv with encoding error handling."""
import json
import duckdb

file_path = "/data/projects/d0bede7f-ba19-407d-8488-86068b98a6be/repo/data/raw/Customers.csv"
conn = duckdb.connect()

# Try to load with ignore_errors to skip bad rows
try:
    conn.execute(f"""
        CREATE TABLE sample AS
        SELECT * FROM read_csv_auto('{file_path}',
                                    ignore_errors=true,
                                    store_rejects=true)
        LIMIT 10000
    """)

    # Check for rejected rows
    try:
        rejects = conn.execute("SELECT COUNT(*) FROM reject_errors").fetchone()[0]
        if rejects > 0:
            print(f"WARNING: {rejects} rows rejected due to errors", file=sys.stderr)
    except:
        rejects = 0

    # Get row count
    row_count = conn.execute("SELECT COUNT(*) FROM sample").fetchone()[0]

    # Get column types via DESCRIBE
    describe = conn.execute("DESCRIBE sample").fetchall()

    # Get sample values and null counts
    columns = []
    for col_name, col_type, *_ in describe:
        samples = conn.execute(
            f'SELECT DISTINCT "{col_name}" FROM sample '
            f'WHERE "{col_name}" IS NOT NULL LIMIT 5'
        ).fetchall()
        sample_values = [str(row[0]) for row in samples]

        null_count = conn.execute(
            f'SELECT COUNT(*) FROM sample WHERE "{col_name}" IS NULL'
        ).fetchone()[0]

        columns.append({
            "name": col_name,
            "inferred_type": col_type,
            "sample_values": sample_values,
            "null_count": null_count,
        })

    # Total row count
    total_rows = conn.execute(
        f"SELECT COUNT(*) FROM read_csv_auto('{file_path}', ignore_errors=true)"
    ).fetchone()[0]

    result = {
        "file_path": file_path,
        "rows_sampled": row_count,
        "total_rows": total_rows,
        "rejected_rows": rejects,
        "columns": columns,
    }

    # Include first 100 rows
    col_names = [c["name"] for c in columns]
    quoted = ', '.join(f'"{n}"' for n in col_names)
    rows = conn.execute(f"SELECT {quoted} FROM sample LIMIT 100").fetchall()
    result["sample_rows"] = [[str(v) if v is not None else "" for v in row] for row in rows]

    print(json.dumps(result, indent=2))

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    import sys
    sys.exit(1)
