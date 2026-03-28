#include <iostream>

class Rational
{
public:
    Rational(int num, int denom)
    {
        numerator = num;

        if(denom==0) denom = 1;
        denominator = denom;
    }

    Rational operator+(const Rational& other) const
    {
        int denom {denominator};
        int num { numerator + other.numerator};

        if(denominator != other.denominator)
        {
            num = numerator * other.denominator + other.numerator * denominator;
            denom = denominator * other.denominator;
        }
        return Rational{num, denom};
    };
    Rational operator*(const Rational& other) const
    {
        int denom {denominator * other.denominator};
        int num { numerator * other.numerator};
        return Rational{num, denom};
    };
    int getNumerator() const { return numerator; }
    int getDenominator() const { return denominator; }
private:
    int numerator, denominator;
};


inline std::ostream& operator<<(std::ostream& stream, const Rational& r)
{
    return stream << r.getNumerator() << "/" << r.getDenominator();
}

int main()
{
    Rational r1{3, 4};
    Rational r2{1, 2};
    Rational r3{r1 + r2};
    std::cout << r3 << std::endl;

    Rational r4{r1 * r2};
    std::cout << r4 << std::endl;

    Rational r5{1, 4};
    Rational r6{r1 + r5};
    std::cout << r6 << std::endl;

    Rational r7{4,0};
    std::cout << r7 << std::endl;
}