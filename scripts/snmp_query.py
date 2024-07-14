import sqlite3
from datetime import datetime
from pysnmp.hlapi import (
    getCmd, SnmpEngine, CommunityData,
    UdpTransportTarget, ContextData, ObjectType, ObjectIdentity
)


def create_database():
    conn = sqlite3.connect('snmp_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS snmp_data
                 (timestamp TEXT, oid TEXT, value TEXT)''')
    conn.commit()
    conn.close()


def insert_data(timestamp, oid, value):
    conn = sqlite3.connect('snmp_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO snmp_data (timestamp, oid, value) VALUES (?, ?, ?)",
              (timestamp, oid, value))
    conn.commit()
    conn.close()


def query_snmp_data():
    iterator = getCmd(SnmpEngine(),
                      CommunityData('public', mpModel=0),
                      UdpTransportTarget(('localhost', 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))

    error_indication, error_status, error_index, var_binds = next(iterator)
    if error_indication:
        print(error_indication)
    elif error_status:
        print('%s at %s' % (error_status.prettyPrint(),
                            error_index and var_binds[int(error_index) - 1][0] or '?'))
    else:
        for var_bind in var_binds:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            oid = var_bind[0].prettyPrint()
            value = var_bind[1].prettyPrint()
            insert_data(timestamp, oid, value)


if __name__ == "__main__":
    create_database()
    query_snmp_data()
