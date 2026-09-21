from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    stage = input("Etapa no funil de vendas: ")

    # validar os dados
    # depois de validado...
    # precisamos modelar os dados do lead como um dict
    print(model_lead(name, email, stage))

    # agora... com meu lead modelado como dict...
    # preciso enviar para o leads.json
    # para isso, vamos usar o control/controller
    control.create_lead(model_lead(name, email, stage))

    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()

    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia")
        return

    # nesse momento, temos que enviar essa query (busca) para o control
    # o control irá comparar a query com os dados de leads.json
    # o retorno do resultado de control será uma lista com os leads encontrados
    search_results = control.read_leads_search(query)

    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def export_leads():
    print("lead exportado")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()