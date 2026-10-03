import logging

# Create a named logger specifically for the Authentication Module
logger = logging.getLogger("VizioneLabs.Auth")

def login_user(username: str, password_hash: str) -> bool:
    logger.info(f"Authenticating user '{username}'...")
    
    if username == "admin":
        logger.warning(f"Admin login detected from IP 192.168.1.50!")
        return True
    elif username == "blocked_user":
        logger.error(f"Authentication failed! Account '{username}' is locked.")
        return False
    else:
        logger.info(f"User '{username}' authenticated successfully.")
        return True