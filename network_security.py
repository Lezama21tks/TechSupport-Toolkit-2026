import socket

def scan_critical_ports():
    # Escáner básico de seguridad para técnicos 2026
    target = "127.0.0.1" 
    critical_ports = [22, 80, 443, 3389, 8069] # SSH, Web, RDP, Odoo
    
    print(f"Verificando puertos críticos en: {target}")
    
    for port in critical_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"ALERTA: Puerto {port} ABIERTO. Verificar firewall.")
        else:
            print(f"Puerto {port}: Protegido.")
        s.close()

if __name__ == "__main__":
    scan_critical_ports()
