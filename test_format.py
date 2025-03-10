def formatar_cabecalho_cena(numero_cena, localizacao, ambiente, descricao):
    cabecalho = f"{numero_cena}. {localizacao} - {ambiente}\n"
    cabecalho += descricao.upper() + "\n"
    return cabecalho

def formatar_acao(texto):
    return texto + "\n"

def formatar_dialogo(personagem, fala):
    return f"{personagem.upper()}\n{fala}\n"

def formatar_transicao(transicao):
    return f"{transicao.upper()}\n"

# Exemplo de uso
roteiro = []

# Cena 1
roteiro.append(formatar_cabecalho_cena(1, "INTERNO", "SALA DE ESTAR - DIA", "Uma sala de estar aconchegante com sofá e TV ligada."))
roteiro.append(formatar_acao("João entra na sala e se senta no sofá, pegando o controle remoto."))
roteiro.append(formatar_dialogo("JOÃO", "Onde está Maria? Ela disse que estaria aqui."))
roteiro.append(formatar_transicao("CORTE PARA:"))

# Cena 2
roteiro.append(formatar_cabecalho_cena(2, "EXTERNO", "JARDIM - DIA", "Um jardim bem cuidado com flores e árvores."))
roteiro.append(formatar_acao("Maria está regando as plantas, distraída."))
roteiro.append(formatar_dialogo("MARIA", "João deve estar procurando por mim..."))
roteiro.append(formatar_transicao("DESVANEECE PARA:"))

# Exibir o roteiro formatado
print("\n".join(roteiro))