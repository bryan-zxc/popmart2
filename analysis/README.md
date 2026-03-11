# Analysis

Python and SQL scripts for data analysis.

Scripts are executed via `run.py` using a `pipeline.yml` configuration that defines execution order, inputs, outputs, and validation checks.

## Script naming conventions

Each table has one creation script named after the table it produces:

| Layer | Prefix | Script | Purpose |
|-------|--------|--------|---------|
| Working | `l10wrk_` | `l10wrk_<name>.py` | Ingest file into DuckDB with typed columns |
| Derived | `l20drv_` | `l20drv_<name>.sql` | Transform from wrk/drv tables |
| Export | `l30exp_` | `l30exp_<name>.sql` | Final tables for reporting consumption |

Layer numbers use gaps (10, 20, 30) to allow custom intermediate layers (e.g. l15, l25).

## Analysis Deliverables

### Scope
- **Analysis Period:** 2020-2021 only (not full 2016-2021 dataset)
- **Base Tables:** 5 l10wrk_ tables (sales, products, customers, stores, exchange_rates)
- **Total Sales Rows (full dataset):** 62,884
- **Expected 2020-2021 Sales:** ~12,238 rows (based on historical distribution)

### 1. Product Line Rationalisation

**Business Goal:** Identify most/least profitable products for discontinuation decisions

**Required Outputs:**
- Product-level profitability (all 2,517 products for 2020-2021 period)
- Category-level profitability rollup (8 categories)
- Subcategory-level profitability rollup (32 subcategories)

**Key Metrics:**
- Revenue USD (converted from all currencies using daily exchange rates)
- Cost USD (unit_cost_usd × quantity)
- Gross Margin USD (revenue - cost)
- Gross Margin % (margin / revenue × 100)
- Units sold
- Orders containing product

**Export Tables:**
- `l30exp_product_profitability` — product-level analysis with profitability rankings
- `l30exp_category_profitability` — category and subcategory rollups

### 2. Store Performance Analysis

**Business Goal:** Rank stores, identify top/bottom performers, compare online vs physical

**Required Outputs:**
- Store ranking by revenue and margin (all 67 stores)
- Top 10 and bottom 10 performers
- Product category mix by store
- Online (store_key=0) vs physical store comparison

**Key Metrics:**
- Revenue USD
- Gross Margin USD
- Gross Margin %
- Units sold
- Average order value
- Revenue per square meter (efficiency metric for physical stores)
- Category mix (% revenue by category)

**Export Tables:**
- `l30exp_store_ranking` — all stores ranked by performance metrics
- `l30exp_store_insights` — top/bottom performers with detailed analysis

**Note:** Store performance based ONLY on sales/margin metrics. No geographical customer matching.

### Data Dependencies

**Required Joins:**
- Sales → Products (via product_key) for profitability calculations
- Sales → Stores (via store_key) for store performance
- Sales → Exchange Rates (via order_date + currency_code) for USD conversion

**Data Quality Prerequisites:**
- Primary key uniqueness verified on all source tables
- Join completeness verified (no orphaned sales records)
- Exchange rate coverage confirmed for all 2020-2021 sales transactions
- Arithmetic safety validated (no division by zero scenarios)
