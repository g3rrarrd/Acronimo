import acronimo as ac

if __name__ == "__main__":
    print("Digite una organizacion o concepto")
    acron = ac.acronimo(input())
    print(acron.convert_text_acro())