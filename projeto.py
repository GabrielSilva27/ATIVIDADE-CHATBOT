# Assistente Virtual - TechStore

def apresentar_opcoes():
    return (
        "\nPosso te ajudar com as seguintes opções:\n"
        "1. Ver produtos disponíveis (ex: celulares, notebooks)\n"
        "2. Saber o horário de funcionamento\n"
        "3. Receber uma recomendação\n"
        "4. Falar com um atendente humano\n"
        "5. Encerrar o atendimento\n"
    )

def recomendar_produto(categoria):
    recomendacoes = {
        "celular": "Recomendo o Xiaomi Redmi Note 13 Pro, ótimo custo-benefício.",
        "notebook": "O notebook Dell Inspiron i5 é uma excelente escolha para produtividade.",
        "fone": "O fone JBL Tune 510BT é uma ótima opção com bluetooth e boa duração de bateria."
    }
    for item in recomendacoes:
        if item in categoria:
            return recomendacoes[item]
    return "No momento, recomendo o Samsung Galaxy A34 — equilibrado entre preço e desempenho."

def responder(pergunta):
    pergunta = pergunta.lower()

    if any(p in pergunta for p in ["olá", "oi", "bom dia", "boa tarde", "boa noite"]):
        return "Olá! Bem-vindo à TechStore." + apresentar_opcoes()

    elif "celular" in pergunta:
        return "Temos celulares Samsung, iPhone e Xiaomi. Deseja uma recomendação específica?"

    elif "notebook" in pergunta:
        return "Temos notebooks Dell, Lenovo e Acer. Posso te ajudar a escolher um?"

    elif "fone" in pergunta or "fone de ouvido" in pergunta:
        return "Temos fones JBL, Xiaomi e Sony — com e sem fio."

    elif "horário" in pergunta or "funcionamento" in pergunta:
        return "Funcionamos de segunda a sexta, das 9h às 18h."

    elif "recomenda" in pergunta or "sugestão" in pergunta:
        return recomendar_produto(pergunta)

    elif "humano" in pergunta or "atendente" in pergunta:
        return "Encaminhando você para um atendente humano... (simulação)"

    elif "sair" in pergunta or "tchau" in pergunta or "encerrar" in pergunta:
        return "Obrigado por visitar a TechStore. Até logo!"

    else:
        return "Desculpe, não entendi. Pode reformular ou escolher uma opção?\n" + apresentar_opcoes()

# Execução principal
print("="*40)
print(" Assistente Virtual da TechStore ".center(40, "="))
print("="*40)
print("Olá! Eu sou seu atendente virtual.")
print("Digite 'sair' a qualquer momento para encerrar.")
print(apresentar_opcoes())

while True:
    entrada = input("\nVocê: ")
    resposta = responder(entrada)
    print("Chatbot:", resposta)
    if "Até logo" in resposta:
        break
