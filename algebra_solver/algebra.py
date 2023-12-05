from sympy import sympify, Eq, solveset
import PySimpleGUIQt as sg

class AlgebraSolver:
    def __init__(self):
        self.result = ""
        self.layout = [
            [sg.Text("Enter the linear equation"), sg.In(key="lneq")],
            [sg.Button("Evaluate", enable_events=True, key="eval")],
            [sg.Text("Result:"), sg.Text(text="", key="result")],
        ]

    def evaluate_linear(self, expression):
        if not expression:
            return "Enter a valid expression"
        try:
            left_side, right_side = expression.split("=")
            sy_exp = sympify(left_side)
            req = sympify(right_side)
        except (SyntaxError, ValueError):
            return "Not a valid linear equation"
        return solveset(Eq(sy_exp, req))

    def render(self):
        window = sg.Window("Algebra Solver", resizable=True, size=(800, 100 + len(self.layout[0][0]) * 10), layout=self.layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "EXIT"):
                break
            elif event == "eval":
                self.result = str(self.evaluate_linear(values["lneq"]))
                window["result"].update(self.result)

if __name__ == "__main__":
    al = AlgebraSolver()
    al.render()
