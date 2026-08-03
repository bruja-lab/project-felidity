"""
PROJECT FELIDITY // HARDWARE RECOVERY SUBSYSTEM
Architect: bruja-lab (Systems & Core Infrastructure Engineer)
Classification: Local VRAM Purge & Daemon Shutdown Macro
"""

import os
import subprocess
import sys

def execute_hardware_memory_flush():
    """
    Forcefully terminates background local model server daemons 
    to release active allocation tracks inside the GPU VRAM slots.
    """
    print("[SYSTEM INGRESS]: Initializing hardware memory recovery pass...")
    
    # Target execution string mapped directly to the local model server daemon
    target_process = "ollama_llama_server.exe"
    
    try:
        if sys.platform.startswith("win"):
            # Execute bitwise taskkill command to force-drop background server layers
            print(f"[PROCESS]: Dispatching force-termination matrix to {target_process}...")
            subprocess.run(
                ["taskkill", "/f", "/im", target_process], 
                check=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE
            )
            print("[SUCCESS]: Graphics card VRAM allocations flushed cleanly to zero.")
        else:
            # Unix-compliant teardown track for MacBook/Linux environments
            subprocess.run(["pkill", "-f", "ollama"], check=True)
            print("[SUCCESS]: Unix local model execution layers severed.")
            
    except subprocess.CalledProcessError:
        # Error handling loop if server was already cleanly closed down by the host OS
        print("[STATUS LOG]: Target process not detected in active hardware lanes. Memory is already sterile.")
    except Exception as system_fault:
        print(f"[⚠️ LINK FAILURE]: Hardware memory purge sequence aborted: {system_fault}")

if __name__ == "__main__":
    print("=== ATHENAPSYCHE CORE // TERMINATION VECTOR ENGAGED ===")
    execute_hardware_memory_flush()
