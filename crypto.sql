CREATE TABLE IF NOT EXISTS crypto
(
    ID                  VARCHAR(20) PRIMARY KEY,
    NAME                VARCHAR(100) NOT NULL,
    SYMBOL              VARCHAR(20) NOT NULL,
    PRICE_USD           FLOAT,
    MARKET_CAP_USD      BIGINT,
    VOLUME_24H_USD      BIGINT
);

