
print("Este é um novo script adicionando uma nova célula.")
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar o modelo e o tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_response(prompt, model, tokenizer, max_length=100, temperature=0.7, top_p=0.9, repetition_penalty=1.1):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.replace(prompt, '').strip()

print("AI: Olá! Como posso ajudar você hoje?")
while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit", "encerrar conversa", "pare"]:
        print("AI: Tchau! Foi bom conversar com você.")
        break
    response = generate_response(user_input, model, tokenizer)
    print("AI:", response)
    