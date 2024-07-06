from pysnmp.hlapi import *

def get_snmp_data(oid, host='localhost', community='public'):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            return varBind[1].prettyPrint()

if __name__ == "__main__":
    print(get_snmp_data('1.3.6.1.2.1.1.1.0'))  # Beispiel OID für sysDescr

