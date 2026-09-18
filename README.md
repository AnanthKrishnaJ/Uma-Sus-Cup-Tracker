# 🏇 UMA SUS CUP TRACKER

> A visual race archive and analytics dashboard for the Uma Sus Cup community.

<p align="center">
  <a href="https://github.com/AnanthKrishnaJ/Uma-Sus-Cup-Tracker">
    <img src="https://img.shields.io/github/stars/AnanthKrishnaJ/Uma-Sus-Cup-Tracker?style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/AnanthKrishnaJ/Uma-Sus-Cup-Tracker">
    <img src="https://img.shields.io/github/forks/AnanthKrishnaJ/Uma-Sus-Cup-Tracker?style=for-the-badge" alt="Forks">
  </a>
  <img src="https://img.shields.io/github/last-commit/AnanthKrishnaJ/Uma-Sus-Cup-Tracker?style=for-the-badge" alt="Last Commit">
</p>

---

## ✦ Overview

**Uma Sus Cup Tracker** is a custom race-tracking system designed to preserve and analyse Uma Sus Cup races.

Instead of keeping race results scattered across Discord messages and screenshots, the tracker brings them together into a single searchable archive.

```text
RACE DATA
    │
    ├── Players
    ├── Uma Musume
    ├── Positions
    ├── Times / Gaps
    ├── Courses
    ├── Weather
    ├── Track Conditions
    └── Strategies
          │
          ▼
    ┌───────────────┐
    │  DATA ENGINE  │
    └───────┬───────┘
            │
      ┌─────┼─────┐
      ▼     ▼     ▼
   Players  Uma  Races
   Stats   Stats Archive
      │     │     │
      └─────┼─────┘
            ▼
     VISUAL DASHBOARD
```

---

## ⚡ Features

| Feature              | Description                         |
| -------------------- | ----------------------------------- |
| 🏆 Race Archive      | Store historical Sus Cup races      |
| 👤 Player Profiles   | Track individual player performance |
| 🐎 Uma Profiles      | Analyse Uma Musume performance      |
| 📊 Statistics        | Wins, podiums, averages and more    |
| ⏱️ Race Times        | Track finish times and gaps         |
| 🏁 Course Analysis   | Compare performance across courses  |
| 🎯 Strategy Analysis | Track racing strategies             |
| 🖼️ Race Gallery     | Preserve race screenshots           |
| 📈 Charts            | Visualise historical performance    |
| 📱 Responsive UI     | Desktop and mobile support          |

---

## 📊 Analytics

The tracker calculates statistics from the stored race data.

### Player Analytics

```text
Wins
Podiums
Top 4
Top 5
Average Finish
Win Rate
Podium Rate
Consistency
Experience
Best Finish
Worst Finish
Best Time
Favourite Course
Best Course
Favourite Strategy
Best Strategy
```

### Uma Analytics

```text
Total Runs
Wins
Podiums
Average Finish
Win Rate
Best Player
Race History
```

### Race Records

```text
Fastest Time
Most Wins
Most Podiums
Best Average Finish
Biggest Winning Margin
Closest Finish
```

---

## 🧩 Technology

```text
Frontend
├── HTML5
├── CSS3
└── JavaScript

Libraries
├── Chart.js
├── Font Awesome
├── Google Fonts
└── html2canvas

Utilities
├── Python
└── JavaScript
```

---

## 📁 Project Structure

```text
Uma-Sus-Cup-Tracker/
│
├── index.html
│
├── data/
│
├── backup_exports/
│
├── *.py
├── *.js
│
├── archive_mascot.png
├── cups.txt
├── cups_info.txt
│
└── README.md
```

The repository also contains supporting scripts used for:

```text
Race verification
Data checking
Data normalization
Cup updates
Ranking updates
Statistics
Winner analysis
Data exports
Historical processing
```

---

## 🚀 Running Locally

Clone the repository:

```bash
git clone https://github.com/AnanthKrishnaJ/Uma-Sus-Cup-Tracker.git
```

Enter the project:

```bash
cd Uma-Sus-Cup-Tracker
```

Open the application:

```text
index.html
```

Or use **VS Code + Live Server** for local development.

---

## 🛠️ Development

Before modifying the tracker:

```bash
git status
```

Create a backup commit:

```bash
git add .
git commit -m "Backup before tracker update"
```

After making changes:

```bash
git add .
git commit -m "Update tracker"
git push
```

---

## 🏁 Race Data Workflow

```text
Discord Race
      │
      ▼
Collect Results
      │
      ▼
Enter / Process Data
      │
      ▼
Validate Data
      │
      ▼
Update Race Archive
      │
      ▼
Recalculate Statistics
      │
      ▼
Dashboard
```

---

## 🎨 Animated Showcase

An animated project showcase is available separately:

```text
/animated/
    └── index.html
```

It provides a presentation-style introduction to the project without modifying the main tracker interface.

---

## 🔮 Future Development

Possible future improvements include:

```text
[ ] Advanced leaderboard
[ ] Automated race import
[ ] Discord integration
[ ] Player comparison
[ ] Uma comparison
[ ] Advanced course analytics
[ ] Season tracking
[ ] Achievement system
[ ] Live race mode
[ ] Cloud database
[ ] Authentication
[ ] Automatic backups
```

---

## 👨‍💻 Author

**Ananth Krishna J.**

GitHub:

```text
https://github.com/AnanthKrishnaJ
```

---

## 📜 License

No separate open-source license is currently specified for this repository.

Unless a license is added, the repository contents remain subject to applicable copyright law.
