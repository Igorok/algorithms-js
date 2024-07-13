class Solution {
int x;
int y;
int gain;
string remainder;

bool checkX (char a, char b) {
    return (a == 'a' && b == 'b');
}
bool checkY (char a, char b) {
    return (a == 'b' && b == 'a');
}
void findAB (char check) {
    int gain = 0;
    bool found = false;

    string remainder = "";
    int i = 0;
    while (i < this->remainder.size() - 1) {
        char a = this->remainder[i];
        char b = this->remainder[i+1];

        if (
            (check == 'x' && this->checkX(a, b))
            || (check == 'y' && this->checkY(a, b))
        ) {
            i += 2;
            gain += (check == 'x' ? this->x : this->y);
            found = true;
        } else {
            remainder += a;
            i += 1;
        }
        if (i == this->remainder.size() - 1)
            remainder += this->remainder[i];
    }

    if (!found) {
        return;
    }

    this->remainder = remainder;
    this->gain += gain;

    this->findAB(check);
}

public:
    int maximumGain(string s, int x, int y) {
        this->gain = 0;
        this->remainder = s;
        this->x = x;
        this->y = y;

        if (x > y) {
            this->findAB('x');
            this->findAB('y');
        } else {
            this->findAB('y');
            this->findAB('x');
        }

        return this->gain;
    }
};
