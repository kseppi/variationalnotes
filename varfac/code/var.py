"""Code implementing variational inference for faculty evaluations network"""
import numpy as np

def get_data():
    """Retrieve faculty evaluations"""
    return [
        6.39,
        6.32,
        6.25,
        6.24,
        6.21,
        6.18,
        6.17,
        6.13,
        6.00,
        6.00,
        5.97,
        5.82,
        5.81,
        5.71,
        5.55,
        5.50,
        5.39,
        5.37,
        5.35,
        5.30,
        5.27,
        4.94,
        4.50]


# pylint: disable-msg=too-many-locals,invalid-name
def _run():
    """Run variational inference

    According to the original problem, the prior belief for the mean is
    N(5, 1/9) and the prior belief for the variance is
    InvGamma(alpha=11, beta=2.5).
    """
    data = get_data()
    data_len = len(data)
    NUM_ITERS = 100
    # parameters for true prior
    mu = 5.0
    sigma2 = 1/9
    alpha = 11
    beta = 2.5
    # constants used at every iteration
    ksigma2 = data_len * sigma2
    data_sum = np.sum(data)
    half_data_sum2 = (data_sum ** 2) / 2
    # parameters for approximation
    m = 5.0
    v = 1/9
    a = alpha + data_len / 2
    b = 2.5
    for _ in range(NUM_ITERS):
        b_div_a = b / a
        # m = (-mu + (b/a) * sigma2 * (sum(data))) / (1 + ((b/a) * sigma2 * K)
        m = (-mu + (b_div_a * sigma2 * data_sum)) / (1 + (b_div_a * ksigma2))
        print('m', m)
        # v = sigma2 / (1 + ((b/a) * sigma2 * K))
        v = sigma2 / (1 + (b_div_a * ksigma2))
        print('v', v)
        # a = alpha + K/2 <- note that a is not dependent on m, v, or b
        # b  = (-2*beta + sum(data^2) - 2*m*sum(data) + K*(m^2+v)) / 2
        b = -beta + half_data_sum2 - (m*data_sum) + (data_len*((m**2)+v)/2)
        print('b', b)
    print('# Variational mean, variance:', m, b/(a-1))
    print('# Sample mean, variance:', np.mean(data), np.var(data))

if __name__ == '__main__':
    _run()
