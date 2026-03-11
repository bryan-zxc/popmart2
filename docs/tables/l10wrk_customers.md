# l10wrk_customers

- **Row count**: 15,266
- **Ingestion script**: [l10wrk_customers.py](../../analysis/l10wrk_customers.py)

## Key Notes

- Source file had latin-1 encoding (German city names with umlauts) — converted to UTF-8 during ingestion
- Each row represents a unique customer
- Customers span 8 countries across 3 continents
- Birth years range from 1935 to 2002

## Columns

### customer_key (INTEGER) — Categorical
- 15,266 distinct values
- Unique (no duplicates)
- Nulls: 0

### gender (VARCHAR) — Categorical
- 2 distinct values: Male (7,748), Female (7,518)
- Nulls: 0

### name (VARCHAR) — Categorical
- 15,118 distinct values
- Top 3: John Smith (4), Mary Williams (3), Michael Thompson (3)
- Nulls: 0

### city (VARCHAR) — Categorical
- 8,258 distinct values
- Top 3: Toronto (204), New York (130), Los Angeles (119)
- Nulls: 0

### state_code (VARCHAR) — Categorical
- 468 distinct values
- Top 3: CA (740), ON (644), IL (597)
- Nulls: 0

### state (VARCHAR) — Categorical
- 512 distinct values
- Top 3: California (715), Ontario (644), Texas (522)
- Nulls: 0

### zip_code (VARCHAR) — Categorical
- 9,505 distinct values
- Top 3: 90017 (70), S4P 3Y2 (50), H3C 5K4 (37)
- Nulls: 0

### country (VARCHAR) — Categorical
- 8 distinct values: United States (6,828), United Kingdom (1,944), Canada (1,553), Germany (1,473), Australia (1,420), Netherlands (733), France (670), Italy (645)
- Nulls: 0

### continent (VARCHAR) — Categorical
- 3 distinct values: North America (8,381), Europe (5,465), Australia (1,420)
- Nulls: 0

### birthday (DATE) — Date
- Range: 1935-02-03 to 2002-02-18
- Nulls: 0 | Special dates (1900/9999): 0
- Count by year: 1935 (182), 1936 (232), 1937 (245), 1938 (217), 1939 (212), 1940 (220), 1941 (223), 1942 (212), 1943 (234), 1944 (216), 1945 (250), 1946 (219), 1947 (203), 1948 (244), 1949 (217), 1950 (228), 1951 (241), 1952 (212), 1953 (220), 1954 (250), 1955 (235), 1956 (235), 1957 (235), 1958 (231), 1959 (243), 1960 (211), 1961 (251), 1962 (234), 1963 (220), 1964 (241), 1965 (241), 1966 (222), 1967 (207), 1968 (264), 1969 (226), 1970 (204), 1971 (230), 1972 (231), 1973 (222), 1974 (212), 1975 (217), 1976 (226), 1977 (247), 1978 (217), 1979 (213), 1980 (253), 1981 (213), 1982 (246), 1983 (220), 1984 (219), 1985 (246), 1986 (220), 1987 (232), 1988 (213), 1989 (214), 1990 (221), 1991 (244), 1992 (237), 1993 (222), 1994 (219), 1995 (234), 1996 (224), 1997 (218), 1998 (224), 1999 (233), 2000 (234), 2001 (271), 2002 (17)
