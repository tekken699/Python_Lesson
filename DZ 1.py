with open("nginx_logs.txt", "r",encoding='utf-8') as f:
    w = list(f)
    ip = []
    get = []
    product = []
    for i in w:
        ip.append(i.split("- -")[-2])
        get.append(i.split(" ")[5])
        product.append(i.replace("HTTP", "").split(" /")[-2])
    for i, q, e in zip(ip, get, product):
        r = i, q, e
        print(r)