def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    means = []

    if mode == "row":

        for row in matrix:
            total = 0

            for value in row:
                total += value

            means.append(total / len(row))

    elif mode == "column":

        for col in range(len(matrix[0])):
            total = 0

            for row in matrix:
                total += row[col]

            means.append(total / len(matrix))

    return means