def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n = len(vectors)
    
    # Step 1: Calculate mean of each vector
    means = []
    
    for vector in vectors:
        total = 0
        
        for value in vector:
            total += value
        
        means.append(total / len(vector))

    # Step 2: Calculate covariance matrix
    covariance_matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            total = 0

            for k in range(len(vectors[i])):
                deviation_i = vectors[i][k] - means[i]
                deviation_j = vectors[j][k] - means[j]

                total += deviation_i * deviation_j

            covariance = total / (len(vectors[i]) - 1)
            row.append(covariance)

        covariance_matrix.append(row)

    return covariance_matrix