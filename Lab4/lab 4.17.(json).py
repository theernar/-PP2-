import json

# Файл жолын дұрыс көрсету
file_path = r"C:\Users\user\Desktop\PP2\Lab4\sample-data.json"

# JSON файлды оқу
with open(file_path, "r") as file:
    data = json.load(file)  # JSON-ды парсинг жасау

# Шыққан нәтижені өңдеу
print("Interface Status")
print("=" * 50)
print("DN".ljust(50) + "Description".ljust(20) + "Speed".ljust(10) + "MTU")
print("-" * 90)

# JSON құрылымындағы "imdata" ішіндегі әр объектіден дерек алу
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"] if "speed" in attributes else "inherit"
    mtu = attributes["mtu"] if "mtu" in attributes else "9150"  # Болжамды мән

    print(dn.ljust(50) + "".ljust(20) + speed.ljust(10) + mtu)
