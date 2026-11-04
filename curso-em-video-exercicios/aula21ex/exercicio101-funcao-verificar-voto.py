def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade <16:
        return f'Com {idade} anos: Não vota'
    if 16 <= idade <18 or idade >65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} ano: Voto obrigatório'


ano = int(input('Digite o seu ano de nascimento: '))
print(voto(ano))