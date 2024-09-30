import streamlit as st
import openai
import os
from dotenv import load_dotenv


# Cargar las variables del archivo .env
load_dotenv()

# Obtener la clave de OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")

# # Verifica que la clave se ha cargado correctamente
# if openai_api_key:
#     print("La clave de OpenAI se ha cargado correctamente.")
# else:
#     print("Error al cargar la clave de OpenAI.")

assert openai_api_key.startswith('sk-'),"Error cargando la key, debe iniciar con sk-"

from openai import OpenAI
client=OpenAI(api_key=openai_api_key)
MODEL='gpt-3.5-turbo'

def gpt_clasificar_sentimiento(prompt, emociones):
    system_prompt = f'''Eres un asistente emocionalmente inteligente.
    Clasifica el sentimiento del texto del usuario con SOLO UNA DE LAS SIGUIENTES EMOCIONES: {emociones}.
    Después de clasificar el texto, responde SOLO con la emoción.'''
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=20, #solo queremos una respuesta
        temperature=0 #tiene que ser deterministico
    )
    
    r=response.choices[0].message.content
    if r=="":
        r='N/A'

    return r


if __name__=="__main__":
    # emociones = 'positivo, negativo'
    # prompt = 'AI will not take over the world'
    # print(gpt_clasificar_sentimiento(prompt=prompt,emociones=emociones))

    col1,col2=st.columns([0.85,0.15])
    with col1:
        st.title("Análisis de Sentimientos")
    with col2:
        st.image("ai.png",width=70)

    with st.form(key="my_form"):
        default_emotions = 'positivo, negativo,neutral'
        emotions=st.text_input('Emociones:',value=default_emotions)
        
        text=st.text_area(label="Texto a clasificar:")
        submit_button=st.form_submit_button(label="Check!")

        if submit_button:
            emotion = gpt_clasificar_sentimiento(prompt=text,emociones=emotions)
            result=f'{text[:50]}=>{emotion}\n'
            st.write(result)

            st.divider()

            if 'history' not in st.session_state:
                if result:
                    st.session_state['history']=result
                else:
                    st.session_state['history']=""
            else:
                st.session_state['history']+=result

            if st.session_state['history']:
                st.text_area(label='History',value=st.session_state['history'],height=400)


