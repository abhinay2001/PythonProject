CREATE TABLE IF NOT EXISTS ingestion_metadata (
    table_name TEXT NOT NULL,
    run_at TIMESTAMP NOT NULL DEFAULT NOW(),
    rows_inserted INT NOT NULL,
    PRIMARY KEY (table_name, run_at)
);
