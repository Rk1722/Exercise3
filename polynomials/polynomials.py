from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub___(self, other):
        if isinstance(Polynomial, Polynomial):
            if self.degree() > other.degree():
                other_coefficients = other.coefficients + [0] * (self.degree()
                                                                 - other.degree
                                                                 ())
                self_coefficients = other_coefficients
            else:
                self_coefficients = self.coefficients + [0] * (other.degree()
                                                               - self.degree())
                other_coefficients = self_coefficients
            result_coefficients = [self_coefficients - other_coefficients for
                                   self_coefficients, other_coefficients in
                                   zip(self.coefficients, other.coefficients)]

            # Remove trailing zeros in the result
            while result_coefficients and result_coefficients[-1] == 0:
                result_coefficients.pop()

            return Polynomial(result_coefficients)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return (self - other)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            final_poly = [0] * (self.degree() + other.degree() + 1)
            for i in range(len(self.coefficients)):
                for j in range(len(other.coefficients)):
                    final_poly[(i+j)] += (self.coefficients[i]
                                          * other.coefficients[j])
        elif isinstance(other, Number):
            final_poly = (self * other)
            final_poly = Polynomial(final_poly)
            return final_poly

    def __rmul__(self, other):
        for i in range(len(self.coefficients)):
            self.coefficent[i] = self.coefficient[i] * other
        return self

    def __pow__(self, other):
        if isinstance(Polynomial, Number):
            if Polynomial == 0:
                final_poly = 0
            else:
                final_poly = 1
                for i in range(other):
                    final_poly *= self
            return final_poly

    def __call__(self, other):
        final_poly1 = 0
        if isinstance(Polynomial, Number):
            for i, coefs in enumerate(self.coefficients):
                final_poly1 += coefs * (other ** (self.degree() - i))
        return final_poly1
