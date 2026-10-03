import logging
from auth_service import login_user
from database_service import execute_query

# ==============================================================================
# GLOBAL CONFIGURATION (Configured ONCE at application start)
# ==============================================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] (%(filename)s:%(lineno)d) -> %(message)s",
    datefmt="%H:%M:%S"
)

# Root/Main Application Logger
logger = logging.getLogger("VizioneLabs.Main")

if __name__ == "__main__":
    print("=" * 85)
    print("VIZIONE LABS — MULTI-MODULE LOGGER ARCHITECTURE DEMO")
    print("=" * 85 + "\n")

    logger.info("Starting Vizione Labs Platform Services...")

    print("\n--- [1] TESTING AUTHENTICATION MODULE ---")
    login_user("lucas", "hash_123")
    login_user("admin", "hash_456")
    login_user("blocked_user", "hash_789")

    print("\n--- [2] TESTING DATABASE MODULE ---")
    execute_query("SELECT * FROM users WHERE id = 101;", timeout=5)
    execute_query("SELECT * FROM financial_records;", timeout=1)
    execute_query("DROP TABLE clients;", timeout=5)

    logger.info("All platform tasks completed successfully.")
    print("\n" + "=" * 85)