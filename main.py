"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/
"""

import openai
import config

openai.api_key = config.api_key

mensajes = [{'role':'system', 'content':'Eres un desarrollador de programación experto'}]


while True:
    contenido = input("Que es lo que quieres saber hoy? ")
    if contenido == 'exit':
        break
    mensajes.append({'role':'user', 'content':contenido})

    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = mensajes)
    response_clean = response.choices[0].message.content
    mensajes.append({'role':'assistant', 'content':response_clean})

    print(response_clean)