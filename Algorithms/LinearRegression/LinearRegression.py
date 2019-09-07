
def calculate_data_mean(data):
    x_sum = 0
    y_sum = 0
    for x, y in data:
        x_sum += x
        y_sum += y
    length = len(data)
    return x_sum/length, y_sum/length

def calculate_weight(x_avg, y_avg, data):
    numerator = 0
    denominator = 0
    for x, y in data:
        numerator += (y - y_avg)*(x - x_avg)
        denominator += (x - x_avg)**2
    return numerator/denominator


def generate_linear_regression_parameter(data):
    x_avg, y_avg = calculate_data_mean(data)
    weight = calculate_weight(x_avg, y_avg, data)
    bias = y_avg - weight * x_avg
    return weight, bias



if __name__ == "__main__":
    data = [
        (1, 2),
        (2, 4),
        (3, 4)
    ]
    print(generate_linear_regression_parameter(data))
