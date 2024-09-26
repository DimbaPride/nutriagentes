from agents.diet_agent import DietAgent

class DietTask:
    def __init__(self, student_info):
        self.agent = DietAgent()
        self.student_info = student_info
        self.description = "Criar um plano de dieta baseado nas informações do aluno."
        self.expected_output = "Plano de dieta otimizado em formato de texto."

    def execute(self):
        return self.agent.create_diet_plan(self.student_info)
