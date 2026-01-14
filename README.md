# 📊 Stats‑Navigator

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Version](https://img.shields.io/github/v/tag/dgrochmal/Stats-Navigator?label=version&sort=semver)
[![Chrome Web Store](https://img.shields.io/badge/Chrome%20Web%20Store-Stats--Navigator-brightgreen)](https://chrome.google.com/webstore/detail/stats-navigator/lbbdpmoliocjdndehobflkmlaemkefpn)
![Last Commit](https://img.shields.io/github/last-commit/dgrochmal/Stats-Navigator)


**Stats‑Navigator** is a Google Chrome extension that lets baseball fans quickly jump between player pages on three major stat sites: *Baseball‑Reference*, *Baseball Savant*, and *Fangraphs*.  
[Chrome Web Store link](https://chrome.google.com/webstore/detail/stats-navigator/lbbdpmoliocjdndehobflkmlaemkefpn)

---

## 🚀 Features

- One‑click navigation between:
  - **Baseball‑Reference**
  - **Baseball Savant**
  - **Fangraphs**
- Detects the current player page and opens the equivalent page on the target site
- Right‑click the extension button to open links in a new tab
- Works on all supported sites and redirects to homepages if not currently on one

---

## 📦 Installation

### Option 1: Install from Chrome Web Store

1. Search for **“Stats Navigator”** on the Chrome Web Store or go [here](https://chrome.google.com/webstore/detail/stats-navigator/lbbdpmoliocjdndehobflkmlaemkefpn).
2. Click **Add to Chrome**.
3. Pin the extension to your toolbar for easy access. 

---

## 🧠 How It Works

When you’re on a player page (e.g., Mike Trout on Baseball‑Reference), clicking the extension:

1. Detects the current site
2. Looks up that player’s ID or searchable name
3. Give you a clickable popup to choose which website you want to go to next.
4. Redirects you to the equivalent page on the selected stat site

Right‑clicking opens the link in a new tab instead of navigating in the current tab.

---

## 🛠 Development & Local Build

If you want to run or modify the extension locally:

1. **Clone the repo:**
   ```bash
   git clone https://github.com/dgrochmal/Stats-Navigator.git
   ```
2. **Open Chrome and go to:**
  `chrome://extensions`
3. **Enable "Developer mode"**
4. Click **Load unpacked**
5. Select the **Stats-Navigator** directory
   
The extension should now appear in your toolbar.

## 🧩 Repository Structure
```kotlin
📁 data
📁 firefox-data
📁 linker-bbref
📁 linker-fangraphs
📁 linker-prospectus
📁 linker-savant
📁 python
📁 zips
📄 icon.png
📄 manifest.json
📄 popup.html
📄 popup.js
```
---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a pull request

Please open an issue for bugs or feature requests.

---

## 🧪 License

This project is released under the **MIT License**.

---

## ☕ Support

If you find Stats‑Navigator useful, consider supporting the developer:

- **Buy Me a Coffee:** [https://www.buymeacoffee.com/dgrochmal](https://www.buymeacoffee.com/dgrochmal)  
- **Venmo:** @Daniel-Grochmal

## 🍿 Video

https://github.com/dgrochmal/Stats-Navigator/assets/demo-video.mp4
