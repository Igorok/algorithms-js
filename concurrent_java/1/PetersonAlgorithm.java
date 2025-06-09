
class PetersonAlgorithm {
    boolean[] wantCs = {false, false};
    int turn = 1;
    public void requestCs (int i) {
        int j = 1 - i;
        wantCs[i] = true;
        turn = j;
        while (wantCs[j] && turn == j) {};
    }
    public void releaseCs (int i) {
        wantCs[i] = false;
    }
}