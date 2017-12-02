import math
import random

if __name__ == '__main__':

    def normal_cdf(x, mu=0, sigma=1):
        return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

    def normal_approximation_to_binomial(n, p):
        mu = p * n
        sigma = math.sqrt(p * (1 - p) * n)
        return mu, sigma

    normal_prob_below = normal_cdf

    def normal_prob_above(x, mu=0, sigma=1):
        return 1 - normal_cdf(x, mu, sigma)

    def normal_prob_between(lo, hi, mu=0, sigma=1):
        return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

    def normal_prob_outside(lo, hi, mu=0, sigma=1):
        return 1 - normal_prob_between(lo, hi, mu, sigma)

    def inverse_normal_cdf(p, mu=0, sigma=0, tolerance=0.00001):

        low_z, low_p = -10.0, 0    # normal_cdf(-10) ~ 0
        hi_z, hi_p = 10.0, 1       # normal_cdf(10) ~ 1
        while hi_z - low_z > tolerance:
            mid_z = (low_z + hi_z) / 2
            mid_p = normal_cdf(mid_z)

            if mid_p < p:
                low_z, low_p = mid_z, mid_p
            elif mid_p > p:
                hi_z, hi_p = mid_z, mid_p
            else:
                break

        return mid_z

    def normal_upper_bound(p, mu=0, sigma=1):  # z for P( Z <= z)
        return inverse_normal_cdf(p, mu, sigma)

    def normal_lower_bound(p, mu=0, sigma=1):  # z for P( Z >= z)
        return inverse_normal_cdf(1 - p, mu, sigma)

    def normal_two_sided_bounds(p, mu=0, sigma=0):   # returns symmetric about the mean
        tail_prob = (1 - p) / 2

        upper_bound = normal_lower_bound(tail_prob, mu, sigma)
        lower_bound = normal_upper_bound(tail_prob, mu, sigma)

        return lower_bound, upper_bound

    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    # null hyp. : p = 0.5 , n= 1000

    # 95% bounds based on assumption p is 0.5 (prob of type 1 error)
    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

    type_2_prob = normal_prob_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_prob  # power < 0.95 to reject null hyp.

    # for one sided (upper tail) if x < x' accept null hyp
    hi = normal_upper_bound(0.95, mu_0, sigma_0)
    type_2_prob = normal_prob_below(hi, mu_1, sigma_1)
    power = 1 - type_2_prob

    def two_sided_p_value(x , mu=0, sigma=1):
        if x >= mu:   # tail is what is greater than x
            return 2 * normal_prob_above(x, mu, sigma)
        else:
            return 2 * normal_prob_below(x, mu, sigma)

    two_sided_p_value(529.5, mu_0, sigma_0)

    # example
    extreme_value_count = 0
    for i in range(100000):
        num_heads = sum(1 if random.random() < 0.5 else 0
                        for _ in range(1000))
        if num_heads >= 530 or num_heads <= 470:
            extreme_value_count += 1

    print(extreme_value_count / 100000)

    two_sided_p_value(531, mu_0, sigma_0)
    upper_p_value = normal_prob_above
    upper_p_value(524.5, mu_0, sigma_0)






















