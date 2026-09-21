from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREATE / READ / UPDATE / DELETE

# READ
def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

# CREATE
def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

# BUSCAR LEADS
def read_leads_search(query):
    """
        Função que recebe uma query (busca de nome ou email) no leads.json
         e RETORNA uma lista com os resultadso
    """
    leads = read_leads()
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]}".lower()

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results