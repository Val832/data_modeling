import sqlite3

# Connexion à la base ou création si elle n'existe pas
conn = sqlite3.connect('data/db/casto.db')
cursor = conn.cursor()

# Création des tables 
cursor.executescript("""
-- Product Table
CREATE TABLE IF NOT EXISTS Product (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    EAN TEXT UNIQUE,
    Name TEXT,
    ShortName TEXT,
    Description TEXT,
    FeatureSummary TEXT,
    ProductStatus TEXT,
    ProductConfiguratorType TEXT,
    SundayDeliveryAvailable BOOLEAN,
    PrimaryCategoryId TEXT,
    PrimaryCategoryName TEXT,
    Purchasable BOOLEAN,
    ContactCentreOrderingOnly BOOLEAN,
    PDPURL TEXT,
    PublishingStatus TEXT,
    DisplayCoverageCalculator BOOLEAN
);

-- Pricing Table
CREATE TABLE IF NOT EXISTS Pricing (
    PricingID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    CurrencyCode TEXT,
    UnitOfMeasure TEXT,
    UnitPriceDisplay BOOLEAN,
    AmountIncTax REAL,
    AmountExTax REAL,
    DeliveryChargeIdentifier TEXT,
    DeliveryChargeThreshold REAL,
    DeliveryChargeAboveThreshold REAL,
    DeliveryChargeBelowThreshold REAL,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Tax Table
CREATE TABLE IF NOT EXISTS Tax (
    TaxID INTEGER PRIMARY KEY AUTOINCREMENT,
    PricingID INTEGER,
    Type TEXT,
    Amount REAL,
    Rate REAL,
    FOREIGN KEY (PricingID) REFERENCES Pricing(PricingID)
);

-- Feature Table
CREATE TABLE IF NOT EXISTS Feature (
    FeatureID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    Description TEXT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Technical Specification Table
CREATE TABLE IF NOT EXISTS TechnicalSpecification (
    TechSpecID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    Name TEXT,
    Value TEXT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Rating Table
CREATE TABLE IF NOT EXISTS Rating (
    RatingID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    Value REAL,
    Count INTEGER,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- URL Table
CREATE TABLE IF NOT EXISTS URL (
    URLID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    SeoId TEXT,
    SeoText TEXT,
    ShareableUrl TEXT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Manual Table
CREATE TABLE IF NOT EXISTS Manual (
    ManualID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    FriendlyName TEXT,
    URL TEXT,
    Type TEXT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);                   
""")

# Commit et fermeture de la connexion 
conn.commit()
conn.close()
