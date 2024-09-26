import streamlit as st
from tasks.diet_task import DietTask
from tasks.workout_task import WorkoutTask
from utils.word_generator import generate_word_doc

st.title('Gerador de Planos de Dieta e Treino')

# Inputs do usuário
student_name = st.text_input('Nome do Aluno')
weight = st.number_input('Peso (kg)', min_value=1.0)
height = st.number_input('Altura (cm)', min_value=1)
goal = st.selectbox('Objetivo', ['Perda de peso', 'Ganho de massa', 'Manutenção'])
diet_restrictions = st.text_input('Restrições Alimentares (opcional)')
physical_restrictions = st.text_input('Restrições Físicas (opcional)')

if st.button('Gerar Plano'):
    student_info = {
        'name': student_name,
        'weight': weight,
        'height': height,
        'goal': goal,
        'diet_restrictions': diet_restrictions,
        'physical_restrictions': physical_restrictions
    }

    # Criação do plano de dieta
    diet_task = DietTask(student_info)
    diet_plan = diet_task.execute()

    # Criação do plano de treino
    workout_task = WorkoutTask(diet_plan, student_info)
    workout_plan = workout_task.execute()

    # Gerar o documento Word
    file_name = generate_word_doc(student_name, diet_plan, workout_plan)
    
    st.success(f'Plano gerado com sucesso! Nome do arquivo: {file_name}')
    st.download_button(label='Baixar Plano', data=open(file_name, 'rb'), file_name=file_name)
