def esponenziazione_veloce(a, e, n):
    d = 1

    # trasformo l'esponenete in binario (è una stringa)
    e_bin = bin(e)[2:]

    for bit in e_bin:
        d = (d * d) % n

        if bit == '1':
            d = (d * a) % n

    return d
def miller_rabin(n, x):
    # definisco n-1 come 2^r * m con m dispari
    m = n - 1
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1

    # calcolo x^m % n  con l'algoritmo di esponenziazione veloce (lo stesso definito per il punto precedente dell'esercizio)
    x = esponenziazione_veloce(x, m, n)

    # se x^m % n == 1 restituisco falso (probabilmente non è composto)
    if x == 1:
        return False

    # se x0 == -1 restituisco falso (probabilmente non è composto)
    if x == n-1:
        return False

    # ciclo fin quando non trovo un x tale che x^2 mod n = -1 (cioè = n-1) oppure fin quando non raggiungo le r iterazioni
    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            return False

    return True

# funzione per inserire i valori
def inserisci_valori():
    x = 0
    while True:
        try:
            n_str = input("Inserisci un numero per testare se è primo con Miller-Rabin (n): ")
            n = int(n_str)

            if n <= 1:
                print("n deve essere maggiore di 1!")
                continue

            if n % 2 == 0:
                print("n deve essere un numero dispari!")
                continue

            x_str = input(f"Inserisci x (1 <= x <= {n - 1}): ")
            x = int(x_str)

            if x < 1 or x >= n:
                print(f"x deve essere compreso tra 1 e {n - 1}!")
                continue

            break
        except ValueError:
            print("Devi inserire un numero intero!")

    return n, x

if __name__ == '__main__':
    n, x = inserisci_valori()
    if miller_rabin(n, x):
        print(f"{n} è composto")
    else:
        print(f"{n} è probabilmente primo.")
