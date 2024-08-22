import subprocess
from flask import Response

TARGET = "localhost"
COMMUNITY = "public"
OID = "1.3.6.1.2.1.1"

def format_for_prometheus(output):
    metrics = []
    for line in output.split('\n'):
        if not line:
            continue

        # Debug: Ausgabe der rohen Zeile
        with open('debug.log', 'a') as f:
            f.write(f"Raw line: {line}\n")

        # Extrahiere die OID und den Wert
        parts = line.split()
        if len(parts) < 4:
            continue

        oid = parts[0]
        value = ' '.join(parts[3:])

        # Debug: Ausgabe von OID und Wert
        with open('debug.log', 'a') as f:
            f.write(f"OID: {oid}, Value: {value}\n")

        # Ersetze Punkte in der OID durch Unterstriche und entferne "iso" Präfix
        metric_name = oid.replace('iso', '').replace('.', '_')

        # Ausgabe im Prometheus-Format
        metrics.append(f"{metric_name} {value}")
    
    return '\n'.join(metrics)

def get_snmp_metrics():
    try:
        output = subprocess.check_output(['snmpwalk', '-v', '2c', '-c', COMMUNITY, TARGET, OID], text=True)
        
        # Debug: Ausgabe der SNMP-Walk-Ergebnisse
        with open('debug.log', 'a') as f:
            f.write(f"SNMP-Walk Output:\n{output}\n")

        # Formatieren der SNMP-Walk-Ausgabe im Prometheus-Format
        formatted_output = format_for_prometheus(output)
        return formatted_output
    except subprocess.CalledProcessError as e:
        return f"Error executing snmpwalk: {e}"