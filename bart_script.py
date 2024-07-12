
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Carregar tokenizador e modelo
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large")

# Função para conversar com o chatbot
def chatbot(texto):
    # Adicionar prefixo 'Usuário:' para a entrada do usuário
    entrada = "Usuário: " + texto
    # Tokenizar entrada
    inputs = tokenizer(entrada, return_tensors="pt")
    # Gerar resposta do modelo
    outputs = model.generate(inputs.input_ids, max_length=150, num_beams=5, early_stopping=True)
    # Decodificar e retornar resposta sem os tokens especiais
    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Remover o prefixo 'Usuário:' da resposta, se presente
    resposta = resposta.replace("Usuário: ", "")
    return resposta

# Interagir com o chatbot
print("Bem-vindo! Vamos conversar.")
while True:
    # Entrada do usuário
    entrada_usuario = input("Você: ")
    # Verificar se o usuário deseja sair
    if entrada_usuario.lower() == 'exit':
        print("Chatbot: Tchau! Foi bom conversar com você.")
        break
    # Obter resposta do chatbot
    resposta_chatbot = chatbot(entrada_usuario)
    # Exibir resposta do chatbot
    print("Chatbot:", resposta_chatbot)

    # adicionando linha de teste para comit por token colab - comit de teste
# adicionand linha teste comit em outra branch
    