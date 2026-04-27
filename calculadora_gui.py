import tkinter as tk
from calculadora import somar, subtrair, multiplicar, dividir, raiz_quadrada


class CalculadoraGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculadora")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self._valor_atual: str = "0"
        self._primeiro_operando: float | None = None
        self._operador: str | None = None
        self._aguardando_operando: bool = False

        self._construir_display()
        self._construir_botoes()

    def _construir_display(self) -> None:
        frame = tk.Frame(self.root, bg="#1e1e2e", padx=12, pady=12)
        frame.pack(fill="x")

        self._label_operacao = tk.Label(
            frame,
            text="",
            anchor="e",
            bg="#1e1e2e",
            fg="#6e6e8e",
            font=("Segoe UI", 13),
        )
        self._label_operacao.pack(fill="x")

        self._label_valor = tk.Label(
            frame,
            text="0",
            anchor="e",
            bg="#1e1e2e",
            fg="#cdd6f4",
            font=("Segoe UI", 36, "bold"),
        )
        self._label_valor.pack(fill="x")

    def _construir_botoes(self) -> None:
        frame = tk.Frame(self.root, bg="#1e1e2e", padx=8, pady=4)
        frame.pack()

        layout = [
            [("C", "limpar"), ("±", "inverter"), ("√", "raiz"), ("÷", "op")],
            [("7", "num"),    ("8", "num"),       ("9", "num"),  ("×", "op")],
            [("4", "num"),    ("5", "num"),       ("6", "num"),  ("−", "op")],
            [("1", "num"),    ("2", "num"),       ("3", "num"),  ("+", "op")],
            [("0", "num"),    (".", "ponto"),      ("=", "igual")],
        ]

        cores = {
            "num":    ("#313244", "#cdd6f4"),
            "op":     ("#f38ba8", "#1e1e2e"),
            "igual":  ("#89b4fa", "#1e1e2e"),
            "limpar": ("#45475a", "#f38ba8"),
            "inverter": ("#45475a", "#cdd6f4"),
            "raiz":   ("#45475a", "#cdd6f4"),
            "ponto":  ("#313244", "#cdd6f4"),
        }

        for linha in layout:
            row_frame = tk.Frame(frame, bg="#1e1e2e")
            row_frame.pack(pady=4)
            for item in linha:
                texto, tipo = item
                bg, fg = cores[tipo]
                largura = 16 if tipo == "igual" else 8
                btn = tk.Button(
                    row_frame,
                    text=texto,
                    width=largura,
                    height=2,
                    bg=bg,
                    fg=fg,
                    activebackground=fg,
                    activeforeground=bg,
                    font=("Segoe UI", 14, "bold"),
                    relief="flat",
                    cursor="hand2",
                    command=lambda t=texto, tp=tipo: self._handle(t, tp),
                )
                btn.pack(side="left", padx=4)

    def _handle(self, texto: str, tipo: str) -> None:
        if tipo == "num":
            self._inserir_digito(texto)
        elif tipo == "ponto":
            self._inserir_ponto()
        elif tipo == "op":
            self._selecionar_operador(texto)
        elif tipo == "igual":
            self._calcular()
        elif tipo == "limpar":
            self._limpar()
        elif tipo == "inverter":
            self._inverter_sinal()
        elif tipo == "raiz":
            self._calcular_raiz()

    def _atualizar_display(self, operacao: str = "") -> None:
        texto = self._valor_atual
        if len(texto) > 12:
            try:
                texto = f"{float(texto):.6g}"
            except ValueError:
                pass
        self._label_valor.config(text=texto)
        self._label_operacao.config(text=operacao)

    def _inserir_digito(self, digito: str) -> None:
        if self._aguardando_operando:
            self._valor_atual = digito
            self._aguardando_operando = False
        elif self._valor_atual == "0":
            self._valor_atual = digito
        else:
            self._valor_atual += digito
        self._atualizar_display()

    def _inserir_ponto(self) -> None:
        if self._aguardando_operando:
            self._valor_atual = "0."
            self._aguardando_operando = False
        elif "." not in self._valor_atual:
            self._valor_atual += "."
        self._atualizar_display()

    def _selecionar_operador(self, op: str) -> None:
        valor = float(self._valor_atual)
        if self._primeiro_operando is not None and not self._aguardando_operando:
            self._calcular(manter_operador=True)
            valor = float(self._valor_atual)
        self._primeiro_operando = valor
        self._operador = op
        self._aguardando_operando = True
        self._atualizar_display(operacao=f"{self._formatar(valor)} {op}")

    def _calcular(self, manter_operador: bool = False) -> None:
        if self._primeiro_operando is None or self._operador is None:
            return
        segundo = float(self._valor_atual)
        a, b = self._primeiro_operando, segundo
        op = self._operador
        operacao_txt = f"{self._formatar(a)} {op} {self._formatar(b)} ="
        try:
            mapa = {"÷": dividir, "×": multiplicar, "−": subtrair, "+": somar}
            resultado = mapa[op](a, b)
            self._valor_atual = self._formatar(resultado)
        except ValueError as e:
            self._valor_atual = "Erro"
            self._atualizar_display(operacao=str(e))
            self._primeiro_operando = None
            self._operador = None
            self._aguardando_operando = True
            return

        self._atualizar_display(operacao=operacao_txt)
        if not manter_operador:
            self._primeiro_operando = None
            self._operador = None
        self._aguardando_operando = True

    def _calcular_raiz(self) -> None:
        valor = float(self._valor_atual)
        try:
            resultado = raiz_quadrada(valor)
            self._atualizar_display(operacao=f"√({self._formatar(valor)}) =")
            self._valor_atual = self._formatar(resultado)
            self._label_valor.config(text=self._valor_atual)
            self._primeiro_operando = None
            self._operador = None
            self._aguardando_operando = True
        except ValueError as e:
            self._valor_atual = "Erro"
            self._atualizar_display(operacao=str(e))
            self._aguardando_operando = True

    def _inverter_sinal(self) -> None:
        if self._valor_atual not in ("0", "Erro"):
            if self._valor_atual.startswith("-"):
                self._valor_atual = self._valor_atual[1:]
            else:
                self._valor_atual = "-" + self._valor_atual
            self._atualizar_display()

    def _limpar(self) -> None:
        self._valor_atual = "0"
        self._primeiro_operando = None
        self._operador = None
        self._aguardando_operando = False
        self._atualizar_display()

    @staticmethod
    def _formatar(valor: float) -> str:
        return str(int(valor)) if valor == int(valor) else f"{valor:g}"


def main() -> None:
    root = tk.Tk()
    CalculadoraGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
