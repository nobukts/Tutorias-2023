palabra = input()

inv_palabra = palabra[::-1]

if palabra == inv_palabra:
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")