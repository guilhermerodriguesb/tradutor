from deep_translator import GoogleTranslator

# Função para selecionar o idioma
def selecionar_idioma():
    idiomas = {
        '1': 'pt',   # Português
        '2': 'en',   # Inglês
        '3': 'es'    # Espanhol
    }
    
    print("Selecione o idioma de origem:")
    print("1. Português")
    print("2. Inglês")
    print("3. Espanhol")
    idioma_origem = input("Digite o número do idioma de origem: ")
    
    print("\nSelecione o idioma de destino:")
    print("1. Português")
    print("2. Inglês")
    print("3. Espanhol")
    idioma_destino = input("Digite o número do idioma de destino: ")
    
    return idiomas[idioma_origem], idiomas[idioma_destino]

# Função principal
def main():
    while True:
        print("\n--- Tradutor Offline ---")
        idioma_origem, idioma_destino = selecionar_idioma()
        
        texto = input("\nDigite o texto que deseja traduzir: ")
        
        # Usar o GoogleTranslator do deep_translator
        traducao = GoogleTranslator(source=idioma_origem, target=idioma_destino).translate(texto)
        print(f"\nTradução: {traducao}")
        
        continuar = input("\nDeseja traduzir outro texto? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
