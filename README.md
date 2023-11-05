# Funx

Funx és un llenguatge de programació orientat a expressions i funcions. Amb Funx podem definir funcions i acabar, opcionalment, amb una expressió.

## Com compilar i executar
Cal posar aquestes comandes per compilar i executar

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor funx.g4
export FLASK_APP=funx
flask run
```

## Extensions del enunciat

He afegit el operador de potencia amb '^'

## Part Visual
He fet servir la inteligencia artificial [chatGPT](https://chat.openai.com/chat) per fer la part visula (el archiu html). Despres l'he anat modificant fins que ha quedat al meu gust.
L'input que vaig fer servir es:

***Tengo un programa en Python y Antrl4 que es un intérprete que reconoce un lenguaje de programación basado en expresiones y funciones llamado Funx.***
***Este intérprete funciona a través de un script en Python donde le puedo pasar o bien expresiones de asignación, evaluación..., o bien puedo declarar funciones o bien puedo llamar a funciones previamente declaradas.***
***Ahora estoy trabajando a través de la terminal, pero me gustaría poder hacerlo visualmente usando flask y jinja2.***
***Podrías generarme un HTML y decirme como modificar el script de Python para que funciones con flask y jinja2 y tenga las siguientes funcionalidades:***

***-Que tenga una recuadro donde se puedan entrar las expresiones para ser evaluadas.***

***-Otro recuadro con los resultados que tenga el siguiente formato:***

***Input:***

***Output:***

***Donde Input es la expresión entrada en formato Funx y el Output es el resultado de evaluar la expresión con el Antrl4.***


***-Finalmente, un recuadro con todas las funciones que han sido declaradas, que vendrán dadas por una variable en el script que se llama tfs y es una lista con el nombre de la función.***

***Me gustaría que fuera bonito y usara una paleta de colores oscura.***
