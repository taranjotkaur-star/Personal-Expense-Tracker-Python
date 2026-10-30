import tkinter as tk


def create_dashboard(parent):

    # Dashboard Main Frame
    dashboard = tk.Frame(parent, bg="#F2F4F8")
    dashboard.pack(fill="x", padx=20, pady=20)

    # Dashboard Heading
    heading = tk.Label(
        dashboard,
        text="Dashboard Overview",
        font=("Arial", 18, "bold"),
        bg="#F2F4F8",
        fg="#263238"
    )
    heading.pack(pady=15)

    # Cards Frame
    cards_frame = tk.Frame(dashboard, bg="#F2F4F8")
    cards_frame.pack(pady=10)

    # Function to Create Cards
    def create_card(title, color):

        card = tk.Frame(
            cards_frame,
            bg="white",
            width=230,
            height=120
        )

        card.pack(side="left", padx=12)
        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#555555"
        ).pack(pady=15)

        amount = tk.Label(
            card,
            text="₹ 0.00",
            font=("Arial", 20, "bold"),
            bg="white",
            fg=color
        )

        amount.pack()

        return amount

    # Create Dashboard Cards
    income_label = create_card(
        "Total Income",
        "#16A085"
    )

    expense_label = create_card(
        "Total Expenses",
        "#E74C3C"
    )

    balance_label = create_card(
        "Available Balance",
        "#2980B9"
    )

    # Return Labels for Updating Values
    return income_label, expense_label, balance_label