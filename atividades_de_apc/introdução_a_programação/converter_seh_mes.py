segundos_totais = int(input())
horas = segundos_totais // 3600
segundos_restantes = segundos_totais % 3600

minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"{horas} h {minutos} m {segundos} s")
