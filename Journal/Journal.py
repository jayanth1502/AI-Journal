import tkinter as tk
from datetime import date

# --- Sample portfolio & changes (you can edit these) ---
portfolio = {"BTC": 60, "ETH": 25, "SOL": 15}
changes = {"BTC": +1.2, "ETH": -1.5, "SOL": +0.5}  # edit values to test

# --- Generate AI Journal ---
def generate_journal():
    today = date.today().strftime("%d %m %Y")
    avg_change = sum(changes.values()) / len(changes)

    best = max(changes, key=changes.get)
    worst = min(changes, key=changes.get)

    journal = f"📓 AI Journal - {today}\n\n"
    journal += f"📊 Avg portfolio change: {avg_change:.2f}%\n"
    journal += f"🚀 Best: {best} ({changes[best]}%)\n"
    journal += f"📉 Worst: {worst} ({changes[worst]}%)\n"
    journal += f"💰 BTC Allocation: {portfolio['BTC']}%\n"

    # Auto-detect performance
    if avg_change > 0:
        journal += "✅ Overall: Positive 📈\n"
    elif avg_change < 0:
        journal += "❌ Overall: Negative 📉\n"
    else:
        journal += "⚖️ Overall: Neutral ➖\n"

    return journal

# --- Show popup ---
def show_popup():
    root = tk.Tk()
    root.title("AI Journal")

    text = tk.Text(root, width=70, height=15, font=("Arial", 12))
    text.insert(tk.END, generate_journal())
    text.configure(state="disabled")
    text.pack(padx=10, pady=10)

    root.mainloop()

# --- Run ---
show_popup()
