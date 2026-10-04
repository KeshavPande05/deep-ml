def determinant_4x4(matrix: list[list[int | float]]) -> float:
    
    def det_3x3(m):
        return (
            m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
        )

    det = 0

    # Expand along the first row
    for col in range(4):

        # Create 3x3 minor
        minor = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]

        # Alternating signs: + - + -
        sign = 1 if col % 2 == 0 else -1

        det += sign * matrix[0][col] * det_3x3(minor)

    return float(det)