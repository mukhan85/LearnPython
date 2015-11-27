from Point import Point


def read_data_points(file_name):
    with open(file_name, "r") as input_file:
        file_content = input_file.readlines()

    data_points = []
    for each_line in file_content:
        each_data_element = each_line.split(sep=",")
        data_points.append(Point(float(each_data_element[0]), float(each_data_element[1])))

    return data_points


# y = mx + b, m = slope, b = y-intercept
def compute_cost(m_a, b_a, points):
    total_error = 0
    for each_point in points:
        total_error += (each_point.y - (m_a * each_point.x + b_a)) ** 2
    return total_error / float(len(points))


def step_gradient(m_current, b_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    num_points = float(len(points))

    for each_point in points:
        x = each_point.x
        y = each_point.y
        b_gradient += -(2 / num_points) * (y - (m_current * x + b_current))
        m_gradient += -(2 / num_points) * x * (y - (m_current * x + b_current))

    new_b = b_current - learning_rate * b_gradient
    new_m = m_current - learning_rate * m_gradient
    return [new_m, new_b]


m = -1
b = 0
data = read_data_points("data.csv")

for num_iter in [100000, 1000000]:
    for i in range(num_iter):
        m, b = step_gradient(m, b, data, 0.0001)
    print("num_iter = {3} : (m = {0}, b = {1}), cost={2}".format(m, b, compute_cost(m, b, data), num_iter))
