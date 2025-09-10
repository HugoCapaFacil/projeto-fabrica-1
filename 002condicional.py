nota1 = float(input("Ensira a Primeira nota: "))
nota2 = float(input("Ensira a Segunda nota: "))
Media = (nota1 + nota2)/2
if Media >= 7:
    print(f"O aluno está Aprovado!, com a media de {Media}")
elif Media > 4:
    print(f"O aluno está de Recuperação, com a media de {Media}")
elif Media < 4:
    print(f"O aluno está reprovado, com a media de {Media}")