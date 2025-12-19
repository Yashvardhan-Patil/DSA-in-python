# calculator.py
import tkinter as tk
from tkinter import messagebox
import ast
import operator as op

# --- Safe expression evaluation using ast ---
# Supported operators mapping
_allowed_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.UAdd: lambda x: x,
    ast.USub: op.neg,
}

def safe_eval(expr: str):
    """
    Safely evaluate a mathematical expression string using ast.
    Supports +, -, *, /, //, %, ** and parentheses and unary +/-
    Raises ValueError for invalid expressions.
    """
    try:
        node = ast.parse(expr, mode='eval')
        return _eval_ast(node.body)
    except Exception as e:
        raise ValueError("Invalid expression") from e

def _eval_ast(node):
    if isinstance(node, ast.BinOp):
        left = _eval_ast(node.left)
        right = _eval_ast(node.right)
        op_type = type(node.op)
        if op_type in _allowed_operators:
            return _allowed_operators[op_type](left, right)
        raise ValueError(f"Unsupported binary operator: {op_type}")
    elif isinstance(node, ast.UnaryOp):
        operand = _eval_ast(node.operand)
        op_type = type(node.op)
        if op_type in _allowed_operators:
            return _allowed_operators[op_type](operand)
        raise ValueError(f"Unsupported unary operator: {op_type}")
    elif isinstance(node, ast.Num):  # Python <3.8
        return node.n
    elif isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numeric constants are allowed")
    elif isinstance(node, ast.Expression):
        return _eval_ast(node.body)
    elif isinstance(node, ast.Call):
        # Disallow function calls
        raise ValueError("Function calls are not allowed")
    else:
        raise ValueError(f"Unsupported expression: {type(node)}")

# --- Tkinter GUI ---
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("360x520")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")

        self._create_widgets()

    def _create_widgets(self):
        # Display entry
        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.entry_var,
                         font=("Segoe UI", 28), bd=0, relief="flat",
                         justify="right", bg="#2b2b2b", fg="#ffffff", insertbackground="white")
        entry.place(x=10, y=20, width=340, height=70)

        # Button style parameters
        btn_font = ("Segoe UI", 18)
        btn_w = 4
        btn_h = 2
        padx = 8
        pady = 8

        # Buttons layout definition: (text, row, col, colspan(optional))
        buttons = [
            ("C", 0, 0), ("DEL", 0, 1), ("%", 0, 2), ("÷", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("×", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("±", 4, 0), ("0", 4, 1), (".", 4, 2), ("=", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("//", 5, 2), ("**", 5, 3),
        ]

        # create button widgets
        start_x = 10
        start_y = 110
        btn_width_px = 80
        btn_height_px = 70

        for text, r, c in buttons:
            x = start_x + c * (btn_width_px + 5)
            y = start_y + r * (btn_height_px + 6)

            bg = "#3a3a3a"
            fg = "white"
            if text in ("C", "DEL"):
                bg = "#d9534f"
            elif text == "=":
                bg = "#ff9500"
            elif text in ("+", "-", "×", "÷", "%", "//", "**"):
                bg = "#4b5563"

            btn = tk.Button(self, text=text, font=btn_font, bd=0, relief="raised",
                            bg=bg, fg=fg, activebackground="#6b6b6b", command=lambda t=text: self._on_button(t))
            btn.place(x=x, y=y, width=btn_width_px, height=btn_height_px)

    def _on_button(self, label: str):
        current = self.entry_var.get()

        if label == "C":
            self.entry_var.set("")
            return
        if label == "DEL":
            # delete last character safely
            self.entry_var.set(current[:-1])
            return
        if label == "=":
            expr = current.replace("×", "*").replace("÷", "/")
            expr = expr.replace(" ", "")
            # support integer division token '//' and power '**', '%' already present
            try:
                result = safe_eval(expr)
            except Exception:
                messagebox.showerror("Error", "Invalid expression")
                return
            # If result is integer-like, show as int
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.entry_var.set(str(result))
            return
        if label == "±":
            # Toggle sign of current number: if entire expression is a number, flip it.
            # Otherwise try to append unary minus if reasonable.
            if current == "":
                self.entry_var.set("-")
                return
            # Try to parse last number and flip its sign
            # naive approach: find last token boundary
            i = len(current) - 1
            while i >= 0 and (current[i].isdigit() or current[i] == '.'):
                i -= 1
            # last number is current[i+1:]
            last_num = current[i+1:]
            if last_num == "":
                # nothing to toggle
                return
            try:
                if "." in last_num:
                    val = float(last_num)
                else:
                    val = int(last_num)
                flipped = str(-val)
                new = current[:i+1] + flipped
                self.entry_var.set(new)
            except Exception:
                # fallback: just insert a unary minus at start
                if current.startswith("-"):
                    self.entry_var.set(current[1:])
                else:
                    self.entry_var.set("-" + current)
            return

        # For operators and digits: map display symbols to internal tokens where needed
        to_insert = label
        if label == "×":
            to_insert = "*"
        elif label == "÷":
            to_insert = "/"
        # We leave '//' and '**' as is
        self.entry_var.set(current + to_insert)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
