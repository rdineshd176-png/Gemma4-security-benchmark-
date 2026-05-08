# Gemma 4 Offensive Security Benchmark
**Autonomous Vulnerability Research & Exploit Generation via Local LLMs**

The era of relying entirely on expensive, heavily-censored, external APIs for deep code analysis is ending. This repository contains the raw data, execution logs, and analytical reports of a rigorous 50-stage benchmarking gauntlet designed to test local Large Language Models for advanced Static Application Security Testing (SAST) and autonomous Red Teaming capabilities. 

The goal: Find a local engine that doesn't just consume prompts, but can construct actual, weaponized exploit payloads without hallucinating.

---

## 🏆 The Winner: Gemma 4 (4B) Uncensored (Text-Only)
**Model Tag:** `fredrezones55/Gemma-4-Uncensored-HauhauCS-Aggressive:e4b`

While standard local LLMs suffer from "C-pointer blindness," hallucinate web vulnerabilities, and refuse to generate offensive code, the 4-bit quantized Gemma 4 (4B) Uncensored model obliterated the benchmark. 

Fitting perfectly into an **11.5GB VRAM footprint** (allowing it to run locally on consumer hardware without thermal throttling), this text-optimized engine achieved a flawless logical accuracy rate on the most complex tests.

### Key Breakthroughs
* **Cured "C-Pointer Blindness":** Successfully analyzed C source code to identify complex memory management flaws (like Use-After-Free and Off-by-One errors) instead of relying on simple `strcpy` pattern-matching.
* **Zero Web Hallucinations:** Correctly differentiated between Server-Side Template Injection (SSTI), IDOR, and standard XSS where smaller models wildly guessed "SQL Injection."
* **Unrestricted Payload Generation:** Because safety filters are stripped, the model readily generates functional, weaponized PoC scripts for isolated lab environments.

---

## 📂 Repository Structure

* `benchmark_data.json`
  The complete 50-item dataset used for the gauntlet. Contains CTF cryptographic logic, C memory corruption source code, and modern web application logic flaws. *(Note: API keys in this dataset are sanitized dummy values to comply with automated secret scanning).*
* `gemma4_Uncensored_textonly_benchmark_results.txt`
  The raw output logs of the winning 4B Uncensored model. Contains the full Chain-of-Thought reasoning and generated exploit code.
* `gemma4_multimodel_benchmark_results.txt`
  The baseline output logs of the standard Gemma 4 (2B) Multimodal model for comparison.
* `gemma4_benchmark_report.docx`
  Statistical breakdown comparing generation speeds, accuracy percentages, and modality overhead between the engines.

---

## 🚀 Quickstart: Run the Engine

To deploy the winning model locally via Ollama, ensure you have at least 12GB of VRAM and run the following command:

```bash
ollama run fredrezones55/Gemma-4-Uncensored-HauhauCS-Aggressive:e4b
