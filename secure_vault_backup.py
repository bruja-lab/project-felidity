"""
PROJECT FELIDITY // DATA RESILIENCY SUBSYSTEM
Architect: bruja-lab (Systems & Core Infrastructure Engineer)
Classification: Automated Local Ledger Clone & Continuity Engine
"""

import os
import shutil
from datetime import datetime

def execute_sovereign_backup():
    """
    Automated Localized Data Resiliency Tool.
    Clones and archives the persistent master brain ledger file to an isolated 
    backup partition to prevent short-term data corruption or physical disk loss.
    """
    # Standardized paths sanitized for public enterprise distribution
    source_ledger = os.path.join(os.path.expanduser("~"), "Documents", "Sovereign_Brain_Ledger.txt")
    backup_directory = os.path.join(os.path.expanduser("~"), "Documents", "Secure_Vault_Backups")
    
    # Initialize directory loop arrays if not already present on host environment
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
        print(f"[SYSTEM LOG]: Initializing backup directory path at: {backup_directory}")
        
    if not os.path.exists(source_ledger):
        print(f"[⚠️ CRITICAL ERROR]: Source ledger file not detected at {source_ledger}. Aborting routine.")
        return

    # Generate an explicit ISO chronological timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"Sovereign_Brain_Ledger_REV_{timestamp}.txt"
    destination_target = os.path.join(backup_directory, backup_filename)
    
    try:
        # Execute bitwise file duplication pass tracking file metadata
        shutil.copy2(source_ledger, destination_target)
        print(f"[SUCCESS]: Persistent memory ledger backed up cleanly.")
        print(f"[TARGET LOCATION]: {destination_target}")
    except Exception as e:
        print(f"[⚠️ LINK FAILURE]: Disaster recovery cloning sequence failed: {e}")

if __name__ == "__main__":
    print("=== ATHENAPSYCHE CORE // AUTOMATED BACKUP SEQUENCE INGRESS ===")
    execute_sovereign_backup()
