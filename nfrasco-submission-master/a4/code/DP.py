#######################     Max Product Problem     ###########################

# The Max Product Problem is stated as follows:

# Given a rope of length n (where n > 2), cut the rope into different parts of 
# lengths less than n such that the product of all the lengths is the 
# maximum possible. 

# i.e. the max product of a rope of length 10 is 3 * 3 * 4 = 36 ... (3 + 3 + 4 = 10)
# ...  the max product of a rope of length 5 is 2 * 3 = 6  ... (2 + 3 = 5)

# This can be written as:
# maxProduct(n) = max(i * (n - i), maxProduct(n - i) * i) for all i in {1, 2, 3 .. n}

##############################################################################

class MaxProductFinder:
    #def __init__(self):
    def findMaxProduct(self, n):
        if n == 0 or n == 1:
            return 0

        max_product = 0
        for i in range(1, n - 1):
            max_product = max(max_product, max(i * (n - i), self.findMaxProduct(n - i) * i))

        return max_product;

    def findMaxProductDP(self, n):
        # TODO : Implement version of max product finder with Dynamic Programming
        if n<= 2: return 0

        l = [0 for _ in range(0, n+1)]

        for i in range(1, n+1):
            maxval = 0

            for j in range(1,i):
                maxval = max(maxval, j * (i-j), j * l[i-j])
            l[i] = maxval
        return l[n]

if __name__ == "__main__":
    f = MaxProductFinder()
    print(f.findMaxProduct(10))
    print(f.findMaxProductDP(1000))