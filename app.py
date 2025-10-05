# app.py
def add(a, b):
    """Additionner deux nombres"""
    return a + b

def multiply(a, b):
    """Multiplier deux nombres"""
    return a * b

def divide(a, b):
    """Diviser deux nombres"""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

def is_palindrome(text):
    """Vérifier si un texte est un palindrome"""
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

def calculate_average(numbers):
    """Calculer la moyenne d'une liste de nombres"""
    if not numbers:
        raise ValueError("La liste ne peut pas être vide")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    print("=== Calculatrice simple ===")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"'radar' est un palindrome: {is_palindrome('radar')}")
    print(f"Moyenne de [10, 20, 30]: {calculate_average([10, 20, 30])}")
