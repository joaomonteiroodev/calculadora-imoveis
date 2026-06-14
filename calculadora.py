import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        valor_imovel = float(entry_imovel.get().replace(",", "."))
        entrada = float(entry_entrada.get().replace(",", "."))
        taxa = float(entry_taxa.get().replace(",", ".")) / 100
        prazo = int(entry_prazo.get())

        if entrada >= valor_imovel:
            messagebox.showerror("Erro", "A entrada não pode ser maior ou igual ao valor do imóvel.")
            return
        if taxa <= 0:
            messagebox.showerror("Erro", "A taxa de juros deve ser maior que zero.")
            return
        if prazo <= 0:
            messagebox.showerror("Erro", "O prazo deve ser maior que zero.")
            return

        financiado = valor_imovel - entrada
        parcela = financiado * (taxa * (1 + taxa) ** prazo) / ((1 + taxa) ** prazo - 1)
        total = parcela * prazo
        juros = total - financiado

        label_financiado.config(text=f"R$ {financiado:,.2f}")
        label_parcela.config(text=f"R$ {parcela:,.2f}")
        label_total.config(text=f"R$ {total:,.2f}")
        label_juros.config(text=f"R$ {juros:,.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

def limpar():
    entry_imovel.delete(0, tk.END)
    entry_entrada.delete(0, tk.END)
    entry_taxa.delete(0, tk.END)
    entry_prazo.delete(0, tk.END)
    label_financiado.config(text="R$ --")
    label_parcela.config(text="R$ --")
    label_total.config(text="R$ --")
    label_juros.config(text="R$ --")

# ── JANELA ────────────────────────────────────────────────────
janela = tk.Tk()
janela.title("Calculadora de Financiamento Imobiliário")
janela.geometry("500x780")
janela.resizable(False, False)
janela.configure(bg="#1a1a2e")

# ── TÍTULO ────────────────────────────────────────────────────
tk.Label(janela, text="🏠 Financiamento Imobiliário",
         bg="#1a1a2e", fg="#ffffff",
         font=("Arial", 16, "bold")).pack(pady=(24, 2))

tk.Label(janela, text="Tabela Price",
         bg="#1a1a2e", fg="#a0a0c0",
         font=("Arial", 10)).pack(pady=(0, 20))

# ── FRAME DOS CAMPOS ──────────────────────────────────────────
frame = tk.Frame(janela, bg="#16213e", bd=0)
frame.pack(padx=30, fill="x")

def campo(parent, label, unidade=""):
    container = tk.Frame(parent, bg="#16213e")
    container.pack(fill="x", padx=20, pady=8)

    tk.Label(container, text=label,
             bg="#16213e", fg="#a0a0c0",
             font=("Arial", 9)).pack(anchor="w")

    entry_frame = tk.Frame(container, bg="#0f3460", bd=0)
    entry_frame.pack(fill="x")

    if unidade:
        tk.Label(entry_frame, text=unidade,
                 bg="#0f3460", fg="#a0a0c0",
                 font=("Arial", 10), padx=8).pack(side="left")

    entry = tk.Entry(entry_frame, bg="#0f3460", fg="#ffffff",
                     font=("Arial", 12), bd=0,
                     insertbackground="white",
                     highlightthickness=1,
                     highlightbackground="#2d5a8e",
                     highlightcolor="#4a90d9")
    entry.pack(fill="x", ipady=8, padx=(0, 8))
    return entry

tk.Label(frame, text="", bg="#16213e").pack(pady=4)
entry_imovel = campo(frame, "Valor do Imóvel", "R$")
entry_entrada = campo(frame, "Valor da Entrada", "R$")
entry_taxa    = campo(frame, "Taxa de Juros Mensal", "%")
entry_prazo   = campo(frame, "Prazo (em meses)", "📅")
tk.Label(frame, text="", bg="#16213e").pack(pady=4)

# ── BOTÕES ────────────────────────────────────────────────────
btn_frame = tk.Frame(janela, bg="#1a1a2e")
btn_frame.pack(pady=16, padx=30, fill="x")

tk.Button(btn_frame, text="Calcular",
          bg="#0f3460", fg="white",
          font=("Arial", 11, "bold"),
          bd=0, padx=20, pady=10,
          activebackground="#1a5276",
          activeforeground="white",
          cursor="hand2",
          command=calcular).pack(side="left", expand=True, fill="x", padx=(0, 6))

tk.Button(btn_frame, text="Limpar",
          bg="#2d2d44", fg="#a0a0c0",
          font=("Arial", 11),
          bd=0, padx=20, pady=10,
          activebackground="#3d3d5c",
          activeforeground="white",
          cursor="hand2",
          command=limpar).pack(side="left", expand=True, fill="x", padx=(6, 0))

# ── RESULTADOS ────────────────────────────────────────────────
res_frame = tk.Frame(janela, bg="#16213e")
res_frame.pack(padx=30, fill="x")

tk.Label(res_frame, text="", bg="#16213e").pack(pady=4)
tk.Label(res_frame, text="RESULTADO",
         bg="#16213e", fg="#4a90d9",
         font=("Arial", 9, "bold")).pack()

def resultado_linha(parent, label):
    row = tk.Frame(parent, bg="#16213e")
    row.pack(fill="x", padx=20, pady=5)
    tk.Label(row, text=label,
             bg="#16213e", fg="#a0a0c0",
             font=("Arial", 10)).pack(side="left")
    valor = tk.Label(row, text="R$ --",
                     bg="#16213e", fg="#ffffff",
                     font=("Arial", 10, "bold"))
    valor.pack(side="right")
    return valor

label_financiado = resultado_linha(res_frame, "💰 Valor Financiado")
label_parcela    = resultado_linha(res_frame, "📆 Parcela Mensal")
label_total      = resultado_linha(res_frame, "💳 Total Pago")
label_juros      = resultado_linha(res_frame, "📈 Total em Juros")

tk.Label(res_frame, text="", bg="#16213e").pack(pady=4)

# ── RODAPÉ ────────────────────────────────────────────────────
tk.Label(janela,
         text="github.com/joaomonteiroodev",
         bg="#1a1a2e", fg="#4a4a6a",
         font=("Arial", 8)).pack(pady=(8, 0))

janela.mainloop()