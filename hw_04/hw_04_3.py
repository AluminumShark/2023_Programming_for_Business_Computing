
n, m = map(int, input().split(","))

matrix = []

for i in range(m):
    input_str = input()
    values = input_str.split(",")
    values = [int(val) for val in values]
    matrix.append(values)

transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
sorted_transposed_matrix = sorted(transposed_matrix, key=lambda x: x[0])
matrix = [[sorted_transposed_matrix[j][i] for j in range(len(sorted_transposed_matrix))] for i in range(len(sorted_transposed_matrix[0]))]

#idle time
idle_time_sum = 0
last_idle = 0
for i in range(1, m):
    current_idle = sum(matrix[i-1])+ last_idle - sum(matrix[i]) + matrix[i][-1]
    idle_time_sum += current_idle
    last_idle = current_idle

print(idle_time_sum)