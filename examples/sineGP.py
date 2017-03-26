import numpy as np
from pyGPGO.GPRegressor import GPRegressor
from pyGPGO.covfunc import squaredExponential
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Build synthetic data (sine function)
    x = np.arange(0, 2 * np.pi + 0.01, step=np.pi / 2.1)
    y = np.sin(x)
    X = np.array([np.atleast_2d(u) for u in x])[:, 0]

    # Specify covariance function
    sexp = squaredExponential()
    # Instantiate GPRegressor class
    gp = GPRegressor(sexp)
    # Fit the model to the data
    gp.fit(X, y)

    # Predict on new data
    xstar = np.arange(0, 2 * np.pi, step=0.01)
    Xstar = np.array([np.atleast_2d(u) for u in xstar])[:, 0]
    ymean, ystd = gp.predict(Xstar, return_std=True)

    # Confidence interval bounds
    lower, upper = ymean - 1.96 * np.sqrt(ystd), ymean + 1.96 * np.sqrt(ystd)

    # Plot values
    plt.figure()
    plt.plot(xstar, ymean, label='Posterior mean')
    plt.plot(xstar, np.sin(xstar), label='True function')
    plt.fill_between(xstar, lower, upper, alpha=0.4, label=r'95\% confidence band')
    plt.grid()
    plt.legend(loc=0)
    plt.show()
