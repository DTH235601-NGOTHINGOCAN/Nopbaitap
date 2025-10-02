def nhap_matrix(rows, cols, name="Matrix"):
    print(f"Nhập các phần tử cho {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Hàng {i+1}: ").split()))
        while len(row) != cols:
            print(f"⚠️ Vui lòng nhập đúng {cols} phần tử.")
            row = list(map(float, input(f"Hàng {i+1}: ").split()))
        matrix.append(row)
    return matrix

def cong_matrix(A, B):
    rows, cols = len(A), len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

def transpose_matrix(M):
    rows, cols = len(M), len(M[0])
    transposed = [[M[j][i] for j in range(rows)] for i in range(cols)]
    return transposed

def in_matrix(M, name="Matrix"):
    print(f"\n{name}:")
    for row in M:
        print(" ".join(map(str, row)))

# --- Chương trình chính ---
if __name__ == "__main__":
    r = int(input("Nhập số hàng: "))
    c = int(input("Nhập số cột: "))

    A = nhap_matrix(r, c, "Matrix A")
    B = nhap_matrix(r, c, "Matrix B")

    # Xuất ma trận A, B
    in_matrix(A, "Matrix A")
    in_matrix(B, "Matrix B")

    # Cộng A + B
    C = cong_matrix(A, B)
    in_matrix(C, "A + B")

    # Hoán vị A và B
    At = transpose_matrix(A)
    Bt = transpose_matrix(B)
    in_matrix(At, "Transpose(A)")
    in_matrix(Bt, "Transpose(B)")
