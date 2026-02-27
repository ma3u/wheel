#!/usr/bin/env python3
"""Simulate 100 mobile joins to the Firebase pending queue."""
import urllib.request, json, time, concurrent.futures

DB_URL = "https://wheel-global-ai-default-rtdb.europe-west1.firebasedatabase.app"

names = [
    "Alice Chen","Bob Martinez","Charlie Kim","Diana Patel","Ethan OBrien",
    "Fiona Schmidt","George Tanaka","Hannah Mueller","Irfan Shah","Julia Costa",
    "Kevin Nguyen","Laura Johansson","Mikhail Petrov","Nina Rossi","Oscar Fernandez",
    "Priya Sharma","Quentin Dubois","Rachel Goldberg","Stefan Muller","Tara OConnor",
    "Umar Khan","Vera Lindqvist","William Park","Xiao Wei","Yuki Sato",
    "Zara Ahmed","Aiden Brooks","Bianca Silva","Carlos Ruiz","Daria Popov",
    "Emil Larsen","Freya Andersen","Gustav Becker","Helena Kowalski","Igor Volkov",
    "Jana Horvat","Karl Fischer","Leila Amari","Marco Ricci","Nadia Khoury",
    "Oliver Wright","Patricia Lopes","Raj Mehta","Sofia Delgado","Thomas Berg",
    "Uma Krishnan","Viktor Novak","Wendy Chang","Xavier Moreau","Yara Haddad",
    "Aleksei Orlov","Beatrice Fontana","Cristian Marin","Daniela Varga","Eduardo Reyes",
    "Fatima ElAmin","Giovanni Russo","Hanna Svensson","Ibrahim Diallo","Jasmine Lee",
    "Kenji Yamamoto","Linnea Eriksson","Manuel Torres","Nora Bakken","Pablo Gutierrez",
    "Quinn Taylor","Rosa Hernandez","Sanjay Iyer","Tatiana Kozlova","Ulrich Weber",
    "Valentina Moreno","Walter Singh","Xiomara Castillo","Youssef Mansour","Zoe Mitchell",
    "Adrian Nowak","Brenda Okafor","Chin Ho Lee","Deepa Nair","Elias Engstrom",
    "Gabriela Soto","Henrik Dahl","Ingrid Lund","JeanPierre Blanc","Katerina Alexiou",
    "Lucas Almeida","Maria Gonzalez","Nikolai Kristensen","Olga Mironova","Pedro Cardoso",
    "Rahul Desai","Simone Bauer","Tomas Nemec","Una Fitzgerald","Vincent Leroy",
    "Wanda Kowalczyk","Xander Stone","Yiannis Papadopoulos","Zainab Hassan","Amira Benali",
]

def clear_db():
    print("Clearing existing data...")
    for path in ["wheel/pending", "wheel/names"]:
        req = urllib.request.Request(DB_URL + "/" + path + ".json", method="DELETE")
        urllib.request.urlopen(req, timeout=10)
    print("Done.\n")

def push_name(i, name):
    ts = int(time.time() * 1000) + i
    payload = json.dumps({"name": name, "ts": ts}).encode()
    req = urllib.request.Request(
        DB_URL + "/wheel/pending.json",
        data=payload,
        method="POST",
        headers={"Content-Type": "application/json"}
    )
    resp = urllib.request.urlopen(req, timeout=15)
    return resp.read()

def check_db():
    time.sleep(2)
    for path in ["wheel/pending", "wheel/names"]:
        r = urllib.request.urlopen(DB_URL + "/" + path + ".json", timeout=10)
        d = json.loads(r.read())
        if d is None:
            print("  " + path + ": empty")
        elif isinstance(d, dict):
            print("  " + path + ": " + str(len(d)) + " entries")
        elif isinstance(d, str):
            c = len([x for x in d.split("\n") if x.strip()])
            print("  " + path + ": " + str(c) + " names on wheel")

if __name__ == "__main__":
    clear_db()

    print("Pushing " + str(len(names)) + " names to Firebase pending queue...")
    t0 = time.time()
    ok = 0
    fail = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        futs = {pool.submit(push_name, i, n): n for i, n in enumerate(names)}
        for f in concurrent.futures.as_completed(futs):
            try:
                f.result()
                ok += 1
            except Exception as e:
                fail += 1
                print("  FAIL " + futs[f] + ": " + str(e))
            if ok > 0 and ok % 25 == 0:
                print("  ..." + str(ok) + " ok")

    elapsed = time.time() - t0
    print("\nDone in " + str(round(elapsed, 1)) + "s: " + str(ok) + " ok, " + str(fail) + " failed")

    print("\nDatabase state:")
    check_db()

    print("\nOpen https://ma3u.github.io/wheel/ to see names auto-added!")
    print("Then click 'Present' to test presenter mode + spin the wheel.")
