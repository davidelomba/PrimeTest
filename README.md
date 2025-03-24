# Miller-Rabin Primality Test

## 📌 Description
This project implements the Miller-Rabin primality test, which is a probabilistic algorithm used to determine if a given number is a prime or composite. The algorithm is based on properties of prime numbers related to modular exponentiation.

The code includes an implementation of fast modular exponentiation (`esponenziazione_veloce()`) to optimize calculations in the Miller-Rabin test.

---

## 📂 Files
- `test_miller_rabin.py`: Contains the implementation of the Miller-Rabin primality test.

---

## ⚙️ Functions

### `esponenziazione_veloce(a, e, n)`
Calculates \(a^e \mod n\) efficiently using the fast exponentiation method (exponentiation by squaring).

### `miller_rabin(n, x)`
Performs a single iteration of the Miller-Rabin primality test on the number `n` with base `x`.
- Returns `True` if `n` is **composite**.
- Returns `False` if `n` is **probably prime**.

### `inserisci_valori()`
Handles user input for the values of `n` and `x`, with validation to ensure the inputs are valid.

---

## 🔍 Usage
Run the program by executing:
```
python test_miller_rabin.py
```

The program will prompt you to enter a number `n` to test for primality and a base `x` satisfying \(1 \leq x \leq n-1\).

### Example:
```
Inserisci un numero per testare se è primo con Miller-Rabin (n): 97
Inserisci x (1 <= x <= 96): 5
97 è probabilmente primo.
```

---

## 📖 Theory
The Miller-Rabin test works by expressing \( n - 1 \) as:
\[
n - 1 = 2^r \times m\quad \text{where } m \text{ is odd}
\]
The algorithm tests whether a given base `x` is a **witness** to the compositeness of `n`. If it fails, then `n` is probably prime.

---

## 💡 Note
The result "probably prime" indicates that the test did not find a witness to compositeness, but this is not a guarantee of primality. To increase accuracy, the test can be repeated with multiple random values of `x`.


