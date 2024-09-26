from openai import OpenAI
from crewai import Agent
from dotenv import load_dotenv
import os

# Carregar as variáveis do .env
load_dotenv()

# Inicializar o cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class DietAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Nutricionista Esportivo",
            goal="Criar uma dieta personalizada com base nas necessidades do aluno.",
            verbose=True,
            memory=True,
            backstory=(
                "Você é um nutricionista esportivo especialista em criar dietas personalizadas "
                "que maximizam os resultados do aluno com base no objetivo fitness."
            )
        )

    def create_diet_plan(self, student_info):
        # Preparar o prompt para a LLM
        prompt = (
            f"Você é um nutricionista esportivo. Crie um plano de dieta personalizado para um aluno com as seguintes informações:\n"
            f"Nome: {student_info['name']}\n"
            f"Peso: {student_info['weight']} kg\n"
            f"Altura: {student_info['height']} cm\n"
            f"Objetivo: {student_info['goal']}\n"
            f"Restrições alimentares: {student_info.get('diet_restrictions', 'Nenhuma')}\n"
            f"Monte um plano de dieta completo e detalhado, incluindo café da manhã, almoço, jantar e lanches."
        )

        # Fazer a chamada para a API GPT-4 usando o cliente instanciado
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um nutricionista esportivo."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extrair e retornar o conteúdo do plano de dieta gerado
        diet_plan = response.choices[0].message.content
        return diet_plan
