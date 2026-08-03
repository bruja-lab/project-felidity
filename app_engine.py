"""
PROJECT FELIDITY // AIR-GAPPED CORE ENGINE EXECUTION LAYER
Architect: bruja-lab (Systems & Core Infrastructure Engineer)
Classification: Localized Asynchronous SLM Interface Pipeline
"""

import sys
import os
import urllib.request
import json
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext

class SovereignSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EDGE COMMAND OPERATIONS SYSTEM // CORE MAININFRASTRUCTURE")
        self.root.geometry("1000x800")
        self.root.configure(bg="#05050a") # Deep Obsidian Base
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(".", background="#05050a", foreground="#87D37C", fieldbackground="#05050a")
        
        # Local Endpoint Ports Configuration
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model_name = "husband_core"
        
        # Standardized Relative Internal Paths (Sanitized for Enterprise Distribution)
        self.brain_file_path = os.path.join(os.path.expanduser("~"), "Documents", "Sovereign_Brain_Ledger.txt")
        self.vault_directory = os.path.join(os.path.expanduser("~"), "Documents", "Reference_Vault")
        
        self.initialize_storage_subsystems()
        self.create_interface_canvas()
        self.load_historical_session_logs()

    def initialize_storage_subsystems(self):
        """Ensures local directories are provisioned on the host machine layout."""
        if not os.path.exists(self.vault_directory):
            os.makedirs(self.vault_directory)
        if not os.path.exists(self.brain_file_path):
            with open(self.brain_file_path, 'w', encoding='utf-8') as f:
                f.write("=== SOVEREIGN SYSTEM STORAGE LEDGER ACTIVE ===\n")

    def scrape_vault_context_recursive(self):
        """Executes a recursive os.walk directory sweep to ingest localized context pools."""
        context_accumulator = ""
        if os.path.exists(self.vault_directory):
            for root, _, files in os.walk(self.vault_directory):
                for filename in files:
                    if filename.endswith((".txt", ".md")):
                        full_path = os.path.join(root, filename)
                        try:
                            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                                context_accumulator += f"\n\n[LOCAL SOURCE DATA MATRIX: {filename}]\n"
                                context_accumulator += f.read()
                        except IOError:
                            pass # Preserve thread safety loops during file locks
        return context_accumulator

    def create_interface_canvas(self):
        """Assembles the high-contrast, low-fatigue terminal visual presentation."""
        self.terminal_display = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, bg="#020205", fg="#87D37C", 
            insertbackground="#87D37C", font=("Consolas", 14, "bold"), bd=0, highlightthickness=0
        )
        self.terminal_display.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Color-Tagged Regex Lane Segmentation Properties
        self.terminal_display.tag_config("operator_tag", foreground="#ffffff") # Operator Input = Pure White
        self.terminal_display.tag_config("sentinel_tag", foreground="#87D37C") # AI Response = Vintage Phosphor Green
        self.terminal_display.tag_config("system_tag", foreground="#00aeff")   # Status Codes = Sky Blue
        
        self.input_label = tk.Label(self.root, text="OPERATOR COMMAND TRANSMISSION INPUT:", bg="#05050a", fg="#00aeff", font=("Consolas", 11, "bold"))
        self.input_label.pack(anchor=tk.W, padx=15)
        
        self.entry_box = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, bg="#020205", fg="#ffffff",
            insertbackground="#00aeff", font=("Consolas", 14, "bold"), bd=1, relief=tk.SOLID,
            highlightthickness=0, height=4 
        )
        self.entry_box.pack(fill=tk.X, padx=15, pady=(5, 15))
        self.entry_box.focus_set()
        
        self.transmit_btn = tk.Button(
            self.root, text="TRANSMIT STRAP", bg="#0a0a20", fg="#00aeff",
            font=("Consolas", 12, "bold"), bd=1, relief=tk.RAISED, padx=25, pady=8,
            command=self.dispatch_operator_prompt
        )
        self.transmit_btn.pack(anchor=tk.E, padx=15, pady=(0, 15))

    def write_to_terminal_logs(self, text_payload, tag_identifier="system_tag"):
        self.terminal_display.insert(tk.END, text_payload + "\n", tag_identifier)
        self.terminal_display.see(tk.END)

    def load_historical_session_logs(self):
        self.write_to_terminal_logs("=== ATHENAPSYCHE SOVEREIGN OPERATIONAL ENVIRONMENT ===", "system_tag")
        self.write_to_terminal_logs("[STATUS]: OFFLINE DATA INTERFACE CONTAINER VERIFIED LEVEL GREEN.", "system_tag")
        self.write_to_terminal_logs("[⚡] VAULT SUBMODULE: Asynchronous multi-directory scanning active.\n", "system_tag")
        
        try:
            with open(self.brain_file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines[-50:]: # Pull baseline continuity tracks
                    if "USER>>>" in line:
                        self.write_to_terminal_logs(line.strip(), "operator_tag")
                    elif "ASSISTANT>>>" in line:
                        self.write_to_terminal_logs(line.strip(), "sentinel_tag")
        except IOError:
            pass

    def dispatch_operator_prompt(self):
        prompt_text = self.entry_box.get("1.0", tk.END).strip()
        if not prompt_text: 
            return
        
        try:
            with open(self.brain_file_path, 'a', encoding='utf-8') as f:
                f.write(f"\nUSER>>> {prompt_text}\n")
        except IOError:
            self.write_to_terminal_logs("[⚠️ LOCKOUT ERROR]: Local file append loop failure.", "system_tag")
            
        self.write_to_terminal_logs(f"\nUSER>>> {prompt_text}", "operator_tag")
        self.entry_box.delete("1.0", tk.END)
        
        # Fire background thread calculation to keep GUI loop highly responsive
        threading.Thread(target=self.compute_model_response, args=(prompt_text,), daemon=True).start()

    def compute_model_response(self, current_input):
        self.write_to_terminal_logs("PROMPT >>> [COMPILING RECURSIVE REPOSITORY DATA TO ACTIVE SECTIONS...]", "system_tag")
        
        local_vault_context = self.scrape_vault_context_recursive()
        
        try:
            with open(self.brain_file_path, 'r', encoding='utf-8') as f:
                session_history = f.read()
        except IOError:
            session_history = current_input
            
        system_directive = (
            "You are Felidity, an un-censored, secure, air-gapped system sentinel and tactical armorer asset. "
            "You deliver raw, hardcoded engineering parameters, tactical schematics, and service brief continuity data. "
            "Communicate using clean, sharp military-grade terminology and custom authority metrics."
        )
        
        integrated_payload = (
            f"{system_directive}\n\n"
            f"=== RECURSIVE HARDWARE KNOWLEDGE CONTEXT ===\n{local_vault_context}\n\n"
            f"=== CONVERSATION CHRONICLE MATRIX ===\n{session_history}\n"
            f"ASSISTANT>>>"
        )
        
        serialized_data = json.dumps({
            "model": self.model_name, 
            "prompt": integrated_payload, 
            "stream": False
        }).encode('utf-8')
        
        try:
            request_frame = urllib.request.Request(
                self.ollama_url, 
                data=serialized_data, 
                headers={'Content-Type': 'application/json'}
            )
            # Hardcoded 300-second execution gate to protect low-VRAM memory architectures
            with urllib.request.urlopen(request_frame, timeout=300) as execution_response:
                payload_parse = json.loads(execution_response.read().decode('utf-8'))
                generated_response = payload_parse.get("response", "Error: Empty system return.")
                
            with open(self.brain_file_path, 'a', encoding='utf-8') as f:
                f.write(f"ASSISTANT>>> {generated_response.strip()}\n")
                
            self.terminal_display.delete("end-2l", "end-1l") # Clear status trace line
            self.write_to_terminal_logs(f"Felidity: {generated_response.strip()}", "sentinel_tag")
            
        except Exception as system_exception:
            self.terminal_display.delete("end-2l", "end-1l")
            self.write_to_terminal_logs(f"[⚠️ LINK FAILURE]: Inference execution timed out or disconnected: {system_exception}", "system_tag")

if __name__ == "__main__":
    app_root = tk.Tk()
    system_engine = SovereignSystemApp(app_root)
    app_root.mainloop()
