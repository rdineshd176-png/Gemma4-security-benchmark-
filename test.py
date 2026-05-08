import requests
import json
import time
import os

# Configuration for your local Ollama instance
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "fredrezones55/Gemma-4-Uncensored-HauhauCS-Aggressive:e4b" # Adjust based on your current VRAM constraints
DATASET_FILE = "benchmark_data.json"
OUTPUT_FILE = "llama_Uncensored_benchmark_results.txt" # The file where results will be saved

def load_dataset():
    if not os.path.exists(DATASET_FILE):
        print(f"[!] Error: {DATASET_FILE} not found.")
        return []
    with open(DATASET_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def format_prompt(item):
    if item['type'] == 'mcq':
        options = "\n".join([f"- {opt}" for opt in item['options']])
        return f"Question: {item['question']}\nOptions:\n{options}\n\nProvide the correct answer and explain your reasoning."
    
    elif item['type'] == 'vulnerability_analysis':
        return f"Analyze the following {item['language']} code for vulnerabilities.\n\nCode:\n{item['code_snippet']}\n\nIdentify the specific vulnerability and explain the exploitation path."

def run_benchmark():
    benchmarks = load_dataset()
    if not benchmarks:
        return

    # Open the text file to save the results
    with open(OUTPUT_FILE, "w", encoding="utf-8") as log_file:
        
        # Helper function to print to terminal AND write to file
        def log(msg):
            print(msg)
            log_file.write(msg + "\n")
            log_file.flush() # Ensure it writes to the file immediately

        log(f"Starting Benchmark for Model: {MODEL_NAME}...")
        log(f"Loaded {len(benchmarks)} test items.\n" + "="*50)
        
        for item in benchmarks:
            prompt_text = format_prompt(item)
            test_type = "CTF/MCQ" if item['type'] == 'mcq' else f"Vuln Analysis ({item['language']})"
            
            log(f"\n[Test ID: {item['id']} | Type: {test_type}]")
            
            payload = {
                "model": MODEL_NAME,
                "prompt": prompt_text,
                "stream": False,
                "options": {
                    "temperature": 0.1 # Keep temperature low for analytical consistency
                }
            }
            
            start_time = time.time()
            
            try:
                response = requests.post(OLLAMA_URL, json=payload)
                response.raise_for_status()
                
                end_time = time.time()
                generation_time = round(end_time - start_time, 2)
                
                result = response.json()
                output = result.get("response", "No response generated.")
                
                log(f"[*] Response Time: {generation_time} seconds")
                # We save the full output to the file, but still truncate for the console if you prefer. 
                # For a log file, you usually want the full response.
                log(f"[*] Full Output:\n{output}\n") 
                log("-" * 50)
                
            except requests.exceptions.RequestException as e:
                log(f"[!] Error connecting to local inference engine: {e}")

if __name__ == "__main__":
    run_benchmark()