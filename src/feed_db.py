import sqlite3
import json

# Fonction pour insérer les données d'un produit dans la base de données
def insert_product_data(product_data):
    try : 
        # Insérer les données du produit
        cursor.execute("""
            INSERT INTO Product (EAN, Name, ShortName, Description, FeatureSummary, ProductStatus, PrimaryCategoryId, PrimaryCategoryName, Purchasable, PDPURL, PublishingStatus, DisplayCoverageCalculator) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            product_data['ean'],
            product_data['name'],
            product_data['shortName'],
            product_data['description'],
            product_data['featureSummary'],
            product_data['productStatus'],
            product_data['primaryCategoryId'],
            product_data['primaryCategoryName'],
            product_data['purchasable'],
            product_data['pdpURL'],
            product_data['publishingStatus'],
            product_data['displayCoverageCalculator'],
        ))

        # Récupérer l'ID du produit qui vient d'être inséré
        product_id = cursor.lastrowid
    
        
        # Insérer les données de tarification
        pricing_data = product_data['pricing']
        cursor.execute("""
            INSERT INTO Pricing (ProductID, CurrencyCode, UnitOfMeasure, UnitPriceDisplay, AmountIncTax, AmountExTax, DeliveryChargeIdentifier, DeliveryChargeThreshold, DeliveryChargeAboveThreshold, DeliveryChargeBelowThreshold) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            product_id,
            pricing_data['currencyCode'],
            pricing_data['unitOfMeasure'],
            pricing_data['unitPriceDisplay'],
            pricing_data['currentPrice']['amountIncTax'],
            pricing_data['currentPrice']['amountExTax'],
            product_data['deliveryChargeIdentifier'],
            float(product_data['deliveryChargeThreshold']),
            float(product_data['deliveryChargeAboveThreshold']),
            float(product_data['deliveryChargeBelowThreshold']),
        ))

        # Récupérer l'ID de tarification qui vient d'être inséré
        pricing_id = cursor.lastrowid
        
        # Insérer les taxes
        for tax in pricing_data['taxes']:
            cursor.execute("""
                INSERT INTO Tax (PricingID, Type, Amount, Rate) 
                VALUES (?, ?, ?, ?)""", (
                pricing_id,
                tax['type'],
                tax['amount'],
                tax['rate'],
            ))

        # Insérer les caractéristiques du produit
        for feature in product_data['features']:
            cursor.execute("""
                INSERT INTO Feature (ProductID, Description) 
                VALUES (?, ?)""", (
                product_id,
                feature,
            ))

        # Insérer les spécifications techniques
        for spec in product_data['technicalSpecifications']:
            cursor.execute("""
                INSERT INTO TechnicalSpecification (ProductID, Name, Value) 
                VALUES (?, ?, ?)""", (
                product_id,
                spec['name'],
                spec['value'],
            ))

        # Insérer les données de rating
        rating_data = product_data['averageRating']
        cursor.execute("""
            INSERT INTO Rating (ProductID, Value, Count) 
            VALUES (?, ?, ?)""", (
            product_id,
            rating_data['value'],
            rating_data['count'],
        ))

        # Insertion des données Manual
        for manual in product_data['manuals'] : 
            cursor.execute("""
                INSERT INTO Manual (ProductID, FriendlyName, URL, Type) 
                VALUES (?, ?, ?, ?)""", (
                product_id,
                manual['friendlyName'],
                manual['url'],
                manual['type']
            ))
            
        url_data = product_data.get('url')
        cursor.execute("""
            INSERT INTO URL (ProductID, SeoId, SeoText, ShareableUrl)
            VALUES (?, ?, ?, ?)""", (
            product_id,
            url_data.get("seoId"),
            url_data.get("seoText"),
            url_data.get("shareableUrl")
        ))

        # Commit après chaque insertion de produit pour sauvegarder les changements
        conn.commit()
    
        return True  # Indique la réussite de l'insertion

    except KeyError as e:
        
        # Retourne False pour indiquer un échec et la nécessité de continuer
        return False
    except Exception as e:
        
        conn.rollback()
        # Retourne False pour indiquer un échec et la nécessité de continuer
        return False

# Charger les données JSON à partir d'un fichier
with open('data/json/data.json', 'r') as file:
    data = json.load(file)

with sqlite3.connect('data/db/casto.db') as conn:
    cursor = conn.cursor()
    
    # Itérer sur chaque produit dans le JSON et insérer dans la base de données
    for product in data:
        success = insert_product_data(product)
        if not success:
            continue
    
    # Le context manager s'occupera de fermer la connexion pour vous.
