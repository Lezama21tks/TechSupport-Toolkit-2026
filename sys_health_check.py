import os
import platform
import shutil
import psutil # En 2026 esta es la librería estándar para monitoreo

def check_system_status():
    print(f"--- Diagnóstico Técnico 2026 - Sistema: {platform.system()} ---")
    
    # 1. Verificar espacio en Disco
    total, used, free = shutil.disk_usage("/")
    print(f"Disco: {used // (2**30)}GB usados de {total // (2**30)}GB")
    
    # 2. Verificar Memoria RAM
    ram = psutil.virtual_memory()
    print(f"RAM: {ram.percent}% en uso")
    
    if ram.percent > 85:
        print("ALERTA: Memoria crítica. Sugerido limpieza de procesos.")

    # 3. Limpieza de archivos temporales (Mantenimiento preventivo)
    print("Iniciando limpieza de logs antiguos...")
    # Lógica de limpieza aquí...

if __name__ == "__main__":
    check_system_status()
