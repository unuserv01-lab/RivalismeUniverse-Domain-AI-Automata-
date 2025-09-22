# RivalismeUniverse: Domain AI Automata

## 🚀 Project Overview

**RivalismeUniverse: Domain AI Automata** is a hackathon platform built for the DoraHacks DomainFi Challenge 2025, merging AI Agents, DeFi, and digital domains into a single ecosystem.

### 🎯 Vision

Transform internet domains into unique AI personas that can:
- Generate and automate content (blogs, posts, tweets)
- Act as bots/agents on social media, Telegram, or Discord
- Tokenize domains via Doma Protocol (as Real World Assets, RWA) for DeFi use cases (collateral, trading, auction)
- Provide analytics & scoring for domains using AI + on-chain data
- Host personalized landing pages for sales, leasing, or community engagement

---

## 🏗️ Repository Structure

```
/rivalismeuniverse
│── README.md
│── docs/
│   └── architecture.md
│── contracts/
│   └── DomainAuction.sol
│── backend/
│   └── app.js
│── frontend/
│   └── pages/index.js
│── ai/
│   └── persona_agent.py
│── bots/
│   └── domain_bot.js
│── analytics/
│   └── domain_scoring.py
│── tests/
│   └── test_auction.js
│── scripts/
│   └── deploy_contract.js
│── package.json
│── hardhat.config.js
```

---

## 📦 Tech Stack

- **Smart contracts:** Solidity + Hardhat (Doma testnet)
- **Backend:** Node.js/Express or Python Flask
- **Frontend:** Next.js + Tailwind
- **AI:** Python (LLM API - OpenAI, Claude, or local)
- **Bots:** Telegram API + Twitter API

---

## ✨ Key Features

1. **Smart Contracts:**  
   - Domain tokenization on Doma testnet  
   - Auction mechanisms (sealed bid, Dutch auction)  
   - Trait/rarity scoring

2. **AI Persona Engine:**  
   - Each domain has a unique persona  
   - Auto-generates content (blog, tweet)  
   - API/webhook responder

3. **Bots & Notifications:**  
   - Telegram bot for domain/auction notifications  
   - X/Twitter bot for automated persona posting

4. **Frontend:**  
   - Dashboard for domain portfolio, auctions, AI persona feed  
   - Landing page generator

5. **Analytics:**  
   - Python scoring model  
   - Visualization on dashboard

---

## ⚡ Quickstart Demo

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Test smart contracts (Hardhat):**
   ```bash
   npx hardhat test
   ```

3. **Run AI persona agent:**
   ```bash
   python ai/persona_agent.py
   ```

---

## 📚 Documentation

See [docs/architecture.md](docs/architecture.md) for architecture details and workflow.

---

## 💡 Hackathon Note

This repo is built for end-to-end demonstration of RivalismeUniverse. Focused on key use-cases:
- Domain auctions (smart contract)
- Simple AI persona bot
- Domain landing page

Modular structure, easy to expand, and ready for integration with various protocols/services.

---

## 🛠️ Contributing

Open for ideas, pull requests, and collaboration!

---

## 🏆 DoraHacks DomainFi Challenge 2025

Part of the innovation for decentralized domain utility, RWA, and AI agent automation.
