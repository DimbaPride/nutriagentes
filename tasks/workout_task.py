from agents.workout_agent import WorkoutAgent

class WorkoutTask:
    def __init__(self, diet_plan, student_info):
        self.agent = WorkoutAgent()
        self.diet_plan = diet_plan
        self.student_info = student_info
        self.description = "Criar um plano de treino que complemente a dieta e maximize os resultados."
        self.expected_output = "Plano de treino otimizado em formato de texto."

    def execute(self):
        return self.agent.create_workout_plan(self.diet_plan, self.student_info)
