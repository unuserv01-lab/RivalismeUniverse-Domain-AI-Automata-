# RivalismeUniverse: Domain AI Automata

## 🚀 Project Overview

**RivalismeUniverse: Domain AI Automata** is a hackathon prototype for the DoraHacks DomainFi Challenge 2025, merging AI Agents, DeFi, and digital domains.

### 🎯 Vision

Transform internet domains into unique AI personas that can:
- Automatically generate content (blogs, posts, tweets)
- Act as bots/agents on social media, Telegram, Discord
- Tokenize domains via Doma Protocol for DeFi use cases (collateral, trading, auction)
- Provide analytics & scoring using AI + on-chain data
- Host personalized landing pages

---

## 🏗️ Repository Structure

```
/RivalismeUniverse-
│── README.md
│── requirements.txt
│── ai/
│   ├── persona_agent.py
│   └── personas.json
│── app/
│   └── server.py
│── contracts/
│   └── DomainAuction.sol
```

---

## 📦 Tech Stack

- **AI Persona Engine:** Python (offline, no API key required)
- **Backend API:** Python Flask (for demo endpoint)
- **Smart Contracts:** Solidity (Doma testnet, auction logic)
- **Frontend:** *(coming soon)*

---

## ✨ Key Features

- **AI Persona Engine:**  
  - Each persona generates creative, monetizable content ideas.
  - Fully offline, deterministic (no paid API required).
- **API Server:**  
  - Demo Flask server exposes persona ideas via endpoint.
- **Smart Contract:**  
  - Minimal Solidity contract for domain auctions.
- **Modular & Hackathon-Ready:**  
  - All components can run independently for demo and extension.

---

## ⚡ Quickstart Demo

### 1. Run AI persona agent offline

```bash
python ai/persona_agent.py
```
Output: Content ideas for each persona (UNUSER, SOLARA, NEXAR).

---

### 2. Launch Flask API server (optional demo)

```bash
pip install flask
python app/server.py
```
Access persona content via browser or HTTP request:
```
http://127.0.0.1:5000/generate/UNUSER
http://127.0.0.1:5000/generate/SOLARA
http://127.0.0.1:5000/generate/NEXAR
```

---

### 3. Review Smart Contract (Solidity)

File: `contracts/DomainAuction.sol`  
You can deploy/test with Hardhat or Remix for auction logic demo.

---

## 📚 Documentation & Next Steps

- Architecture docs *(coming soon)* in `docs/`
- Frontend dashboard *(coming soon)*
- Integration with Doma Protocol *(planned)*

---

## ✅ Status: Ready for Demo & Presentation!

- **Repo is clean, modular, and easy to test.**
- **No API key or paid service required.**
- **Can be presented fully offline or via local server.**
- **Easy to expand for hackathon or real-world MVP.**

---

## 💡 Hackathon Note

Focused on:
- AI persona content engine
- Minimal API server
- Smart contract demo
- Modular structure (easy to expand)

---

## 🛠️ Contributing

Open for ideas, pull requests, and collaboration!

---

## 🏆 DoraHacks DomainFi Challenge 2025

Pushing decentralized domain utility, real-world asset tokenization, and AI agent automation.

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
