# RivalismeUniverse: Domain AI Automata

## 🚀 Project Overview

**RivalismeUniverse: Domain AI Automata** is a hackathon platform for the DoraHacks DomainFi Challenge 2025, merging AI Agents, DeFi, and digital domains.

### 🎯 Vision

Transform internet domains into unique AI personas that can:
- Generate and automate content (blogs, posts, tweets)
- Act as bots/agents on social media, Telegram, or Discord
- Tokenize domains via Doma Protocol for DeFi use cases (collateral, trading, auction)
- Provide analytics & scoring for domains using AI + on-chain data
- Host personalized landing pages

---

## 🏗️ Current Repository Structure

```
/RivalismeUniverse-
│── README.md
│── ai/
│   ├── persona_agent.py
│   └── personas.json
```

---

## 📦 Tech Stack

- **AI Persona Engine:** Python (offline, no API key required)
- **Smart contracts:** Solidity/Hardhat (coming soon)
- **Backend:** Python Flask (optional demo server)
- **Frontend:** (coming soon)

---

## ✨ Key Features (Demo Stage)

- **AI Persona Engine:**  
  - Each domain/persona can auto-generate creative content ideas.
  - Offline, deterministic, and customizable for hackathon/demo.
  - No paid API needed.

---

## ⚡ Quickstart Demo

**Run AI persona agent locally:**

1. Install Python (3.8+ recommended)
2. Download repo & go to project folder:

   ```bash
   git clone https://github.com/unuserv01-lab/RivalismeUniverse-.git
   cd RivalismeUniverse-
   ```

3. Run persona agent (no API key needed):

   ```bash
   python ai/persona_agent.py
   ```

4. You will see detailed content ideas for each persona (UNUSER, SOLARA, NEXAR).

**(Optional) Run Flask server for API endpoint:**

1. Install Flask:

   ```bash
   pip install flask
   ```

2. Run server:

   ```bash
   python app/server.py
   ```

3. Access persona content via:

   ```
   http://127.0.0.1:5000/generate/UNUSER
   http://127.0.0.1:5000/generate/SOLARA
   http://127.0.0.1:5000/generate/NEXAR
   ```

---

## 📚 Documentation

See [docs/architecture.md](docs/architecture.md) *(coming soon)* for details.

---

## 💡 Hackathon Note

This repo is for end-to-end demonstration:
- Domain auctions (smart contract, coming soon)
- Simple AI persona agent (offline, ready)
- Modular structure, easy to expand!

---

## 🛠️ Contributing

Open for ideas, pull requests, and collaboration.

---

## 🏆 DoraHacks DomainFi Challenge 2025

Innovation for decentralized domain utility, RWA, and AI agent automation.
