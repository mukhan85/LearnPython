import numpy as np
import math
from sklearn.datasets.samples_generator import make_regression
from scipy import stats


# to install nympy.
# C:\BLKDeveloper\Learn\LearnPython\venv\Scripts\pip3.4.exe install "C:\Software\numpy\numpy-1.9.3+mkl-cp34-none-win_amd64.whl"

def gradient_descent(alpha, x, y, ep=0.0001, max_iter=10000):
    converged = False
    iter = 0
    m = x.shape[0]  # number of samples

    # initial theta
    t0 = np.random.random(x.shape[1])
    t1 = np.random.random(x.shape[1])

    # total error, J(theta)
    J = sum([(t0 + t1 * x[i] - y[i]) ** 2 for i in range(m)])
    print('Total error: ', J)

    # Iterate Loop
    while not converged:
        # for each training sample, compute the gradient (d/d_theta j(theta))
        grad0 = 1.0 / m * sum([(t0 + t1 * x[i] - y[i]) for i in range(m)])
        grad1 = 1.0 / m * sum([(t0 + t1 * x[i] - y[i]) * x[i] for i in range(m)])

        # update the theta_temp
        temp0 = t0 - alpha * grad0
        temp1 = t1 - alpha * grad1

        # update theta
        t0 = temp0
        t1 = temp1

        # mean squared error
        e = sum([(t0 + t1 * x[i] - y[i]) ** 2 for i in range(m)])

        if abs(J - e) <= ep:
            print('Converged, iterations: ', iter, '!!!')
            converged = True

        J = e  # update error
        iter += 1  # update iter

        if iter == max_iter:
            print('Max interactions exceeded!')
            converged = True

    return t0, t1


if __name__ == '__main__':
    x, y = make_regression(n_samples=100, n_features=1, n_informative=1,
                           random_state=0, noise=35)
    print('x.shape = %s y.shape = %s' % (x.shape, y.shape))

    alpha = 0.01  # learning rate
    ep = 0.01  # convergence criteria

    # call gredient decent, and get intercept(=theta0) and slope(=theta1)
    theta0, theta1 = gradient_descent(alpha, x, y, ep, max_iter=1000)
    print(theta0, theta1)

    J = sum([(theta0 + theta1 * x[i] - y[i]) ** 2 for i in range(x.shape[0])])
    print("Error after regression:", J, math.sqrt(J[0]))

    # check with scipy linear regression
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[:, 0], y)
    print(intercept, slope, r_value, p_value, slope_std_error)

    print("Done!")
