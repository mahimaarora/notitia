import math

if __name__ == '__main__':

    def vector_add(v, w):
        return [v_i + w_i for v_i, w_i in zip(v,w)]

    def vector_subtract(v, w):
        return [v_i - w_i for v_i, w_i in zip(v, w)]

    """def vector_sum(vectors):
        result = vectors[0]
        for vec in vectors[1:]:
            result = vector_add(result, vec)
        return result"""


    def vector_sum(vectors):
        return reduce(vector_add, vectors)

    # vector_sum= partial(reduce,vector_add)

    def scalar_multiply(c, v):
        return [c * v_i for v_i in v]

    def vector_mean(vectors):
        return scalar_multiply(1/len(vectors), vector_sum(vectors))

    def dot_product(v, w):
        return sum(v_i * w_i for v_i, w_i in zip(v,w))

    def sum_of_squares(v):
        return dot_product(v, v)

    def magnitude(v):
        return math.sqrt(sum_of_squares(v))

    def distance(v, w):
        return magnitude(vector_subtract(v, w))

