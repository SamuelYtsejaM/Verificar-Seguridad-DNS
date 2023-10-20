import dns.resolver

def revisarDmarc(domain):
    try:
        answers = dns.resolver.query('_dmarc.' + domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                if txt_string.startswith(b"v=DMARC"):
                    return True
    except dns.resolver.NXDOMAIN:
        return False
    return False

def revisarSpf(domain):
    try:
        answers = dns.resolver.query(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                if txt_string.startswith(b"v=spf"):
                    return True
    except dns.resolver.NXDOMAIN:
        return False
    return False

if __name__ == "__main__":
    domain = "google.com"
    has_dmarc = revisarDmarc(domain)
    has_spf = revisarSpf(domain)

    if has_dmarc:
        print(f"{domain} tiene un registro DMARC.")
    else:
        print(f"{domain} no tiene un registro DMARC.")

    if has_spf:
        print(f"{domain} tiene un registro SPF.")
    else:
        print(f"{domain} no tiene un registro SPF.")