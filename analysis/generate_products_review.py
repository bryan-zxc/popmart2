"""Generate type review HTML for Products table."""
import json
from pathlib import Path

# Read the full sample output to get first 100 rows
sample_file_output = {
    "total_rows": 2517,
    "total_cols": 10
}

# Build review data - note Unit Cost/Price need DOUBLE not VARCHAR (will clean $ signs)
review_data = {
    "table_name": "l10wrk_products",
    "columns": [
        {"original": "ProductKey", "sql_name": "product_key", "recommended": "INTEGER", "classification": "categorical"},
        {"original": "Product Name", "sql_name": "product_name", "recommended": "VARCHAR", "classification": "categorical"},
        {"original": "Brand", "sql_name": "brand", "recommended": "VARCHAR", "classification": "categorical"},
        {"original": "Color", "sql_name": "color", "recommended": "VARCHAR", "classification": "categorical"},
        {"original": "Unit Cost USD", "sql_name": "unit_cost_usd", "recommended": "DOUBLE", "classification": "numeric"},
        {"original": "Unit Price USD", "sql_name": "unit_price_usd", "recommended": "DOUBLE", "classification": "numeric"},
        {"original": "SubcategoryKey", "sql_name": "subcategory_key", "recommended": "VARCHAR", "classification": "categorical"},
        {"original": "Subcategory", "sql_name": "subcategory", "recommended": "VARCHAR", "classification": "categorical"},
        {"original": "CategoryKey", "sql_name": "category_key", "recommended": "VARCHAR", "classification": "categorical"},
        {"original": "Category", "sql_name": "category", "recommended": "VARCHAR", "classification": "categorical"}
    ],
    "sample_rows": [
        ["1", "Contoso 512MB MP3 Player E51 Silver", "Contoso", "Silver", "$6.62 ", "$12.99 ", "0101", "MP4&MP3", "01", "Audio"],
        ["2", "Contoso 512MB MP3 Player E51 Blue", "Contoso", "Blue", "$6.62 ", "$12.99 ", "0101", "MP4&MP3", "01", "Audio"],
        ["3", "Contoso 1G MP3 Player E100 White", "Contoso", "White", "$7.40 ", "$14.52 ", "0101", "MP4&MP3", "01", "Audio"],
        ["4", "Contoso 2G MP3 Player E200 Silver", "Contoso", "Silver", "$11.00 ", "$21.57 ", "0101", "MP4&MP3", "01", "Audio"],
        ["5", "Contoso 2G MP3 Player E200 Red", "Contoso", "Red", "$11.00 ", "$21.57 ", "0101", "MP4&MP3", "01", "Audio"],
        ["6", "Contoso 2G MP3 Player E200 Black", "Contoso", "Black", "$11.00 ", "$21.57 ", "0101", "MP4&MP3", "01", "Audio"],
        ["7", "Contoso 2G MP3 Player E200 Blue", "Contoso", "Blue", "$11.00 ", "$21.57 ", "0101", "MP4&MP3", "01", "Audio"],
        ["8", "Contoso 4G MP3 Player E400 Silver", "Contoso", "Silver", "$30.58 ", "$59.99 ", "0101", "MP4&MP3", "01", "Audio"],
        ["9", "Contoso 4G MP3 Player E400 Black", "Contoso", "Black", "$30.58 ", "$59.99 ", "0101", "MP4&MP3", "01", "Audio"],
        ["10", "Contoso 4G MP3 Player E400 Green", "Contoso", "Green", "$30.58 ", "$59.99 ", "0101", "MP4&MP3", "01", "Audio"],
        ["11", "Contoso 4G MP3 Player E400 Orange", "Contoso", "Orange", "$30.58 ", "$59.99 ", "0101", "MP4&MP3", "01", "Audio"],
        ["12", "Contoso 4GB Flash MP3 Player E401 Blue", "Contoso", "Blue", "$35.72 ", "$77.68 ", "0101", "MP4&MP3", "01", "Audio"],
        ["13", "Contoso 4GB Flash MP3 Player E401 Black", "Contoso", "Black", "$35.72 ", "$77.68 ", "0101", "MP4&MP3", "01", "Audio"],
        ["14", "Contoso 4GB Flash MP3 Player E401 Silver", "Contoso", "Silver", "$35.72 ", "$77.68 ", "0101", "MP4&MP3", "01", "Audio"],
        ["15", "Contoso 4GB Flash MP3 Player E401 White", "Contoso", "White", "$35.72 ", "$77.68 ", "0101", "MP4&MP3", "01", "Audio"],
        ["16", "Contoso 8GB Super-Slim MP3/Video Player M800 White", "Contoso", "White", "$50.56 ", "$109.95 ", "0101", "MP4&MP3", "01", "Audio"],
        ["17", "Contoso 8GB Super-Slim MP3/Video Player M800 Red", "Contoso", "Red", "$50.56 ", "$109.95 ", "0101", "MP4&MP3", "01", "Audio"],
        ["18", "Contoso 8GB Super-Slim MP3/Video Player M800 Green", "Contoso", "Green", "$50.56 ", "$109.95 ", "0101", "MP4&MP3", "01", "Audio"],
        ["19", "Contoso 8GB Super-Slim MP3/Video Player M800 Pink", "Contoso", "Pink", "$50.56 ", "$109.95 ", "0101", "MP4&MP3", "01", "Audio"],
        ["20", "Contoso 8GB MP3 Player new model M820 Black", "Contoso", "Black", "$61.62 ", "$134.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["21", "Contoso 8GB MP3 Player new model M820 Blue", "Contoso", "Blue", "$61.62 ", "$134.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["22", "Contoso 8GB MP3 Player new model M820 Yellow", "Contoso", "Yellow", "$61.62 ", "$134.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["23", "Contoso 8GB MP3 Player new model M820 White", "Contoso", "White", "$61.62 ", "$134.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["24", "Contoso 16GB Mp5 Player M1600 Blue", "Contoso", "Blue", "$91.93 ", "$199.90 ", "0101", "MP4&MP3", "01", "Audio"],
        ["25", "Contoso 16GB Mp5 Player M1600 Black", "Contoso", "Black", "$91.93 ", "$199.90 ", "0101", "MP4&MP3", "01", "Audio"],
        ["26", "Contoso 16GB Mp5 Player M1600 Green", "Contoso", "Green", "$91.93 ", "$199.90 ", "0101", "MP4&MP3", "01", "Audio"],
        ["27", "Contoso 16GB Mp5 Player M1600 White", "Contoso", "White", "$91.93 ", "$199.90 ", "0101", "MP4&MP3", "01", "Audio"],
        ["28", "Contoso 16GB Mp5 Player M1600 Red", "Contoso", "Red", "$91.93 ", "$199.90 ", "0101", "MP4&MP3", "01", "Audio"],
        ["29", "Contoso 32GB Video MP3 Player M3200 White", "Contoso", "White", "$84.49 ", "$255.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["30", "Contoso 32GB Video MP3 Player M3200 Red", "Contoso", "Red", "$84.49 ", "$255.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["31", "Contoso 32GB Video MP3 Player M3200 Orange", "Contoso", "Orange", "$84.49 ", "$255.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["32", "Contoso 32GB Video MP3 Player M3200 Pink", "Contoso", "Pink", "$84.49 ", "$255.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["33", "Contoso 32GB Video MP3 Player M3200 Black", "Contoso", "Black", "$84.49 ", "$255.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["34", "Contoso 4GB Portable MP3 Player M450 Black", "Contoso", "Black", "$48.92 ", "$95.95 ", "0101", "MP4&MP3", "01", "Audio"],
        ["35", "Contoso 4GB Portable MP3 Player M450 White", "Contoso", "White", "$48.92 ", "$95.95 ", "0101", "MP4&MP3", "01", "Audio"],
        ["36", "Contoso 4GB Portable MP3 Player M450 Yellow", "Contoso", "Yellow", "$48.92 ", "$95.95 ", "0101", "MP4&MP3", "01", "Audio"],
        ["37", "Contoso 8GB Clock & Radio MP3 Player X850 Silver", "Contoso", "Silver", "$99.14 ", "$299.23 ", "0101", "MP4&MP3", "01", "Audio"],
        ["38", "Contoso 8GB Clock & Radio MP3 Player X850 Black", "Contoso", "Black", "$99.14 ", "$299.23 ", "0101", "MP4&MP3", "01", "Audio"],
        ["39", "Contoso 8GB Clock & Radio MP3 Player X850 Green", "Contoso", "Green", "$99.14 ", "$299.23 ", "0101", "MP4&MP3", "01", "Audio"],
        ["40", "Contoso 8GB Clock & Radio MP3 Player X850 Blue", "Contoso", "Blue", "$99.14 ", "$299.23 ", "0101", "MP4&MP3", "01", "Audio"],
        ["41", "Contoso 16GB New Generation MP5 Player M1650 Silver", "Contoso", "Silver", "$106.69 ", "$232.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["42", "Contoso 16GB New Generation MP5 Player M1650 White", "Contoso", "White", "$106.69 ", "$232.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["43", "Contoso 16GB New Generation MP5 Player M1650 Black", "Contoso", "Black", "$106.69 ", "$232.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["44", "Contoso 16GB New Generation MP5 Player M1650 blue", "Contoso", "Blue", "$106.69 ", "$232.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["45", "Contoso 16GB New Generation MP5 Player M1650 Pink", "Contoso", "Pink", "$106.69 ", "$232.00 ", "0101", "MP4&MP3", "01", "Audio"],
        ["46", "WWI 1GB Pulse Smart pen E50 White", "Wide World Importers", "White", "$76.45 ", "$149.95 ", "0104", "Recording Pen", "01", "Audio"],
        ["47", "WWI 1GBPulse Smart pen E50 Black", "Wide World Importers", "Black", "$76.45 ", "$149.95 ", "0104", "Recording Pen", "01", "Audio"],
        ["48", "WWI 1GB Pulse Smart pen E50 Silver", "Wide World Importers", "Silver", "$76.45 ", "$149.95 ", "0104", "Recording Pen", "01", "Audio"],
        ["49", "WWI 2GB Pulse Smart pen M100 White", "Wide World Importers", "White", "$91.95 ", "$199.95 ", "0104", "Recording Pen", "01", "Audio"],
        ["50", "WWI 2GB Pulse Smart pen M100 Black", "Wide World Importers", "Black", "$91.95 ", "$199.95 ", "0104", "Recording Pen", "01", "Audio"],
        ["51", "WWI 2GB Pulse Smart pen M100 Blue", "Wide World Importers", "Blue", "$91.95 ", "$199.95 ", "0104", "Recording Pen", "01", "Audio"],
        ["52", "WWI 2GB Pulse Smart pen M100 Silver", "Wide World Importers", "Silver", "$91.95 ", "$199.95 ", "0104", "Recording Pen", "01", "Audio"],
        ["53", "WWI 4GB Video Recording Pen X200 Black", "Wide World Importers", "Black", "$98.07 ", "$296.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["54", "WWI 4GB Video Recording Pen X200 Red", "Wide World Importers", "Red", "$98.07 ", "$296.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["55", "WWI 4GB Video Recording Pen X200 Pink", "Wide World Importers", "Pink", "$98.07 ", "$296.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["56", "WWI 4GB Video Recording Pen X200 Yellow", "Wide World Importers", "Yellow", "$98.07 ", "$296.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["57", "WWI 1GB Digital Voice Recorder Pen E100 Black", "Wide World Importers", "Black", "$79.53 ", "$156.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["58", "WWI 1GB Digital Voice Recorder Pen E100 Red", "Wide World Importers", "Red", "$79.53 ", "$156.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["59", "WWI 1GB Digital Voice Recorder Pen E100 Pink", "Wide World Importers", "Pink", "$79.53 ", "$156.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["60", "WWI 1GB Digital Voice Recorder Pen E100 White", "Wide World Importers", "White", "$79.53 ", "$156.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["61", "WWI 2GB Spy Video Recorder Pen M300 Black", "Wide World Importers", "Black", "$83.24 ", "$181.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["62", "WWI 2GB Spy Video Recorder Pen M300 White", "Wide World Importers", "White", "$83.24 ", "$181.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["63", "WWI 2GB Spy Video Recorder Pen M300 Blue", "Wide World Importers", "Blue", "$83.24 ", "$181.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["64", "WWI 2GB Spy Video Recorder Pen M300 Silver", "Wide World Importers", "Silver", "$83.24 ", "$181.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["65", "WWI 2GB Spy Video Recorder Pen M300 Purple", "Wide World Importers", "Purple", "$83.24 ", "$181.00 ", "0104", "Recording Pen", "01", "Audio"],
        ["66", "NT Bluetooth Stereo Headphones E52 Blue", "Northwind Traders", "Blue", "$13.10 ", "$25.69 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["67", "NT Bluetooth Stereo Headphones E52 Black", "Northwind Traders", "Black", "$13.10 ", "$25.69 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["68", "NT Bluetooth Stereo Headphones E52 Yellow", "Northwind Traders", "Yellow", "$13.10 ", "$25.69 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["69", "NT Bluetooth Stereo Headphones E52 Pink", "Northwind Traders", "Pink", "$13.10 ", "$25.69 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["70", "NT Wireless Bluetooth Stereo Headphones E102 Silver", "Northwind Traders", "Silver", "$22.05 ", "$47.95 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["71", "NT Wireless Bluetooth Stereo Headphones E102 Black", "Northwind Traders", "Black", "$22.05 ", "$47.95 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["72", "NT Wireless Bluetooth Stereo Headphones E102 Blue", "Northwind Traders", "Blue", "$22.05 ", "$47.95 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["73", "NT Wireless Bluetooth Stereo Headphones E102 White", "Northwind Traders", "White", "$22.05 ", "$47.95 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["74", "NT Bluetooth Active Headphones E202 Black", "Northwind Traders", "Black", "$17.45 ", "$37.95 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["75", "NT Bluetooth Active Headphones E202 White", "Northwind Traders", "White", "$17.45 ", "$37.95 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["76", "NT Bluetooth Active Headphones E202 Red", "Northwind Traders", "Red", "$17.45 ", "$37.95 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["77", "NT Bluetooth Active Headphones E202 Silver", "Northwind Traders", "Silver", "$17.45 ", "$37.95 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["78", "NT Wireless Bluetooth Stereo Headphones E302 Silver", "Northwind Traders", "Silver", "$18.65 ", "$40.55 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["79", "NT Wireless Bluetooth Stereo Headphones E302 White", "Northwind Traders", "White", "$18.65 ", "$40.55 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["80", "NT Wireless Bluetooth Stereo Headphones E302 Yellow", "Northwind Traders", "Yellow", "$18.65 ", "$40.55 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["81", "NT Wireless Bluetooth Stereo Headphones E302 Black", "Northwind Traders", "Black", "$18.65 ", "$40.55 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["82", "NT Wireless Bluetooth Stereo Headphones E302 Pink", "Northwind Traders", "Pink", "$18.65 ", "$40.55 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["83", "NT Wireless Bluetooth Stereo Headphones M402 Silver", "Northwind Traders", "Silver", "$45.98 ", "$99.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["84", "NT Wireless Bluetooth Stereo Headphones M402 Red", "Northwind Traders", "Red", "$45.98 ", "$99.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["85", "NT Wireless Bluetooth Stereo Headphones M402 Green", "Northwind Traders", "Green", "$45.98 ", "$99.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["86", "NT Wireless Bluetooth Stereo Headphones M402 Black", "Northwind Traders", "Black", "$45.98 ", "$99.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["87", "NT Wireless Bluetooth Stereo Headphones M402 Purple", "Northwind Traders", "Purple", "$45.98 ", "$99.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["88", "NT Wireless Transmitter and Bluetooth Headphones M150 Black", "Northwind Traders", "Black", "$49.69 ", "$149.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["89", "NT Wireless Transmitter and Bluetooth Headphones M150 Blue", "Northwind Traders", "Blue", "$49.69 ", "$149.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["90", "NT Wireless Transmitter and Bluetooth Headphones M150 Silver", "Northwind Traders", "Silver", "$49.69 ", "$149.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["91", "NT Wireless Transmitter and Bluetooth Headphones M150 Green", "Northwind Traders", "Green", "$49.69 ", "$149.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["92", "NT Wireless Transmitter and Bluetooth Headphones M150 Red", "Northwind Traders", "Red", "$49.69 ", "$149.99 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["93", "WWI Stereo Bluetooth Headphones E1000 Blue", "Wide World Importers", "Blue", "$34.36 ", "$67.40 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["94", "WWI Stereo Bluetooth Headphones E1000 Black", "Wide World Importers", "Black", "$34.36 ", "$67.40 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["95", "WWI Stereo Bluetooth Headphones E1000 Silver", "Wide World Importers", "Silver", "$34.36 ", "$67.40 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["96", "WWI Stereo Bluetooth Headphones E1000 White", "Wide World Importers", "White", "$34.36 ", "$67.40 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["97", "WWI Stereo Bluetooth Headphones E1000 Green", "Wide World Importers", "Green", "$34.36 ", "$67.40 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["98", "WWI Wireless Bluetooth Stereo Headphones M170 Silver", "Wide World Importers", "Silver", "$55.18 ", "$120.00 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["99", "WWI Wireless Bluetooth Stereo Headphones M170 Black", "Wide World Importers", "Black", "$55.18 ", "$120.00 ", "0106", "Bluetooth Headphones", "01", "Audio"],
        ["100", "WWI Wireless Bluetooth Stereo Headphones M170 White", "Wide World Importers", "White", "$55.18 ", "$120.00 ", "0106", "Bluetooth Headphones", "01", "Audio"]
    ],
    "total_rows": sample_file_output["total_rows"],
    "total_cols": sample_file_output["total_cols"]
}

# Read template
template_path = Path(".claude/skills/create-work-table/assets/type-review-template.html")
template = template_path.read_text()

# Inject data
html = template.replace("{{REVIEW_DATA}}", json.dumps(review_data))

# Write output
output_path = Path("data/reviews/l10wrk_products.html")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(html)

print(f"Review page written to: {output_path}")
