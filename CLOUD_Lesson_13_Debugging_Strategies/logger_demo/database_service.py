import logging

# Create a named logger specifically for the Database Module
logger = logging.getLogger("VizioneLabs.Database")

def execute_query(sql_query: str, timeout: int) -> bool:
    logger.info(f"Executing query: '{sql_query}'...")
    
    if timeout < 2:
        logger.warning(f"Short query timeout specified ({timeout}s). Query might time out!")
        
    if "DROP TABLE" in sql_query.upper():
        logger.error(f"CRITICAL SECURITY RISK: Destructive query blocked! SQL: '{sql_query}'")
        return False
        
    logger.info("Query executed successfully.")
    return True