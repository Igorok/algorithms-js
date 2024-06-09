#include <iostream>
#include <vector>

using std::vector;

int get_refills (int milesPerTank, vector<int> gasStations) {
	int refills = 0;
	int pastRefil = 0;
	int size = gasStations.size();

	for (int i = 0; i < size; ++i) {
		if (gasStations[i] - pastRefil > milesPerTank) {
			return -1;
		}
		if (i + 1 == size) {
			return refills;
		}

		if (
			gasStations[i] - pastRefil <= milesPerTank &&
			gasStations[i + 1] - pastRefil > milesPerTank
		) {
			pastRefil = gasStations[i];
			refills += 1;
			continue;
		}
	}

	return refills;
}

int main() {
	int distance;
	int milesPerTank;
	int n;

	std::cin >> distance >> milesPerTank >> n;

	vector<int> gasStations;

	for (int i = 0; i < n; ++i) {
		int dist;
		std::cin >> dist;
		gasStations.push_back(dist);
	}
	gasStations.push_back(distance);

	int refills = get_refills(milesPerTank, gasStations);

	std::cout << refills << "\n";

	return 0;
}