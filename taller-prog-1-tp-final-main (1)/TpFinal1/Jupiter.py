import matplotlib.pyplot as plt
ips_visitas = {
    "192.168.1.1": 120,
    "192.168.1.2": 75,
    "192.168.1.3": 50,
    "192.168.1.4": 30,
    "192.168.1.5": 25
}
plt.figure(figsize=(10, 6))
plt.bar(ips_visitas.keys(), ips_visitas.values(), color='skyblue')
plt.xlabel("IPs")
plt.ylabel("Cantidad de accesos")
plt.title("Cantidad de accesos por IP")
plt.xticks(rotation=45)
plt.show()
