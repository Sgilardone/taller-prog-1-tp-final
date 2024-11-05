archivo_log = "web-server-log.txt"
ips_visitas = {}
paginas_visitas = {}
total_accesos = 0
accesos_exitosos = 0
with open(archivo_log, "r") as file:
    for linea in file:
        partes = linea.split()
        ip = partes[0]
        codigo = partes[-2]
        pagina = partes[6]
        if ip in ips_visitas:
            ips_visitas[ip] += 1
        else:
            ips_visitas[ip] = 1
        if pagina in paginas_visitas:
            paginas_visitas[pagina] += 1
        else:
            paginas_visitas[pagina] = 1
        total_accesos += 1
        if codigo == "200":
            accesos_exitosos += 1
print("Cantidad de accesos por IP:")
for ip, cantidad in ips_visitas.items():
    print(f"{ip}: {cantidad} veces")
paginas_mas_visitadas = sorted(paginas_visitas.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nLas 3 páginas más visitadas:")
for pagina, visitas in paginas_mas_visitadas:
    print(f"{pagina}: {visitas} visitas")
porcentaje_exitosos = (accesos_exitosos / total_accesos) * 100
print(f"\nPorcentaje de accesos exitosos (código 200): {porcentaje_exitosos:.2f}%")