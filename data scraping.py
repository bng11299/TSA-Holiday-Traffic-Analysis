import pandas as pd
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_tsa_data():
    """Scrape TSA passenger volume data from their website."""
    
    # Set up Chrome driver (make sure chromedriver is in your PATH)
    driver = webdriver.Chrome()
    
    try:
        # Navigate to the TSA passenger volumes page
        url = "https://www.tsa.gov/travel/passenger-volumes"
        driver.get(url)
        
        # Wait for the table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        
        # Find all tables on the page
        tables = driver.find_elements(By.TAG_NAME, "table")
        print(f"Found {len(tables)} tables on the page")
        
        all_data = []
        
        for table in tables:
            # Extract data from each table
            rows = table.find_elements(By.TAG_NAME, "tr")
            
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 2:
                    date_str = cells[0].text.strip()
                    passengers_str = cells[1].text.strip()
                    
                    # Clean and convert passenger numbers
                    passengers = passengers_str.replace(',', '')
                    if passengers.isdigit():
                        all_data.append({
                            'date': date_str,
                            'passengers': int(passengers)
                        })
        
        return pd.DataFrame(all_data)
        
    finally:
        driver.quit()

# Scrape the data
print("Scraping TSA data...")
tsa_df = scrape_tsa_data()
print(f"Scraped {len(tsa_df)} records")

def clean_tsa_data(df):
    """Clean and preprocess the TSA data."""
    
    # Create a copy to avoid modifying the original
    df_clean = df.copy()
    
    # Convert date string to datetime
    df_clean['date'] = pd.to_datetime(df_clean['date'])
    
    # Sort by date
    df_clean = df_clean.sort_values('date').reset_index(drop=True)
    
    # Check for missing dates
    date_range = pd.date_range(
        start=df_clean['date'].min(),
        end=df_clean['date'].max(),
        freq='D'
    )
    
    missing_dates = set(date_range) - set(df_clean['date'])
    if missing_dates:
        print(f"Found {len(missing_dates)} missing dates")
        # Create DataFrame for missing dates
        missing_df = pd.DataFrame({'date': list(missing_dates)})
        # Merge with original data
        df_clean = pd.concat([df_clean, missing_df], ignore_index=True)
        df_clean = df_clean.sort_values('date').reset_index(drop=True)
    
    # Handle missing passenger values (forward fill then backward fill)
    df_clean['passengers'] = df_clean['passengers'].fillna(method='ffill').fillna(method='bfill')
    
    # Remove any potential duplicates
    df_clean = df_clean.drop_duplicates(subset=['date']).reset_index(drop=True)
    
    return df_clean

# Clean the data
print("Cleaning data...")
tsa_clean = clean_tsa_data(tsa_df)
print(f"Final dataset has {len(tsa_clean)} records")
print(f"Date range: {tsa_clean['date'].min()} to {tsa_clean['date'].max()}")


