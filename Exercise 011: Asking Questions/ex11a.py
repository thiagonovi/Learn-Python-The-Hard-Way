print("Qual o seu nome?", end=' ')
nome = input()

print("Qual curso você faz?", end=' ')
curso = input()

print("Em que ano ele vai acabar?", end=' ')
ano = input()

txt_final = "Seu nome é {}, você cursa {} e vai se formar em {}"
print(txt_final.format(nome, curso, ano))

print(f"Seu nome é {nome}, você cursa {curso} e vai se formar em {ano}")
