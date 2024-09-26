from openai import OpenAI
from crewai import Agent
from dotenv import load_dotenv
import os

# Carregar as variáveis do .env
load_dotenv()

# Inicializar o cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class WorkoutAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Treinador Esportivo",
            goal="Montar um plano de treino otimizado que complemente a dieta.",
            verbose=True,
            memory=True,
            backstory=(
                "Você é um treinador esportivo com experiência em criar planos de treino "
                "alinhados às necessidades nutricionais e objetivos de performance."
            )
        )

    def create_workout_plan(self, diet_plan, student_info):
        # Preparar o prompt para a LLM
        prompt = (
            f"Você é um treinador esportivo. Com base neste plano de dieta:\n{diet_plan}\n"
            f"Crie um plano de treino personalizado para um aluno com as seguintes informações:\n"
            f"Nome: {student_info['name']}\n"
            f"Peso: {student_info['weight']} kg\n"
            f"Altura: {student_info['height']} cm\n"
            f"Objetivo: {student_info['goal']}\n"
            f"Restrições físicas: {student_info.get('physical_restrictions', 'Nenhuma')}\n"
            f"Monte um plano de treino completo e detalhado para otimizar os resultados."
        )

        # Fazer a chamada para a API GPT-4 usando o cliente instanciado
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um treinador esportivo."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extrair e retornar o conteúdo do plano de treino gerado
        workout_plan = response.choices[0].message.content
        return workout_plan
