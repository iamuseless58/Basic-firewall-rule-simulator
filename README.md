# 🔥 Firewall Rule Simulator (GUI)

A Python-based GUI Firewall Rule Simulator using Tkinter, designed to allow users to define basic firewall rules and test incoming packets against them.



## 🎯 Features

- Add firewall rules (IP, port, protocol, ALLOW/DENY)
- Check incoming packets against defined rules
- Simple GUI using `tkinter`
- Auto-saving and loading of rules (in JSON format)



## 🖼️ Screenshots

You can add screenshots in the `screenshots/` folder and link them here.



## 🗃️ Folder Structure


firewall-rule-simulator/
├── firewall_simulator_gui.py       # Main application
├── firewall_rules.json             # Auto-generated rule database
├── README.md                       # Project documentation
├── requirements.txt                # Python libraries required
└── screenshots/                    # GUI screenshots (optional)


##🚀 How to Run

### 🖥️ Requirements
- Python 3.x
- Tkinter (pre-installed with most Python installations)

### 🔧 Install dependencies

bash
pip install tk


> Note: `tkinter` is often already installed with Python. This step is usually optional.

### ▶️ Run the app

```bash
python firewall_simulator_gui.py
```

---

## 📦 Future Enhancements

- IP range/block support
- Export logs to CSV
- Advanced rule prioritization
- CLI + GUI dual support



## ⚠️ Disclaimer

This tool is built for educational purposes only and simulates the logic of firewall systems. It is not intended to replace real-world security systems.
