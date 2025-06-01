import java.util.Arrays;


class SortArr extends Thread {
    int[] numbers;
    int[] result;

    public SortArr(int[] _numbers) {
        numbers = _numbers;
        result = new int[numbers.length];
    }

    public int[] getResult() {
        return result;
    }

    public void run () {
        if (numbers.length < 2) {
            result = numbers;
            return;
        }

        int middle = Math.round(numbers.length / 2);
        int[] left = Arrays.copyOfRange(numbers, 0, middle);
        int[] right = Arrays.copyOfRange(numbers, middle, numbers.length);

      	// Creating Thread
        SortArr t1 = new SortArr(left);
        SortArr t2 = new SortArr(right);
        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            System.out.println("t1 message is: " + e.getMessage());
        }

        int[] r1 = t1.getResult();
        int[] r2 = t2.getResult();

        // int[] result = new int[numbers.length];
        int i = 0;
        int j = 0;


        while (i < r1.length && j < r2.length) {
            if (r1[i] <= r2[j]) {
                result[i+j] = r1[i];
                i += 1;
            } else {
                result[i+j] = r2[j];
                j += 1;
            }
        }

        while (i < r1.length) {
            result[i+j] = r1[i];
            i += 1;
        }

        while (j < r2.length) {
            result[i+j] = r2[j];
            j += 1;
        }

        System.out.println(
            "Not Main thread is: " +
            Thread.currentThread().getName() +
            " numbers " + numbers +
            " result " + result
        );
    }

    public static void main(String[] args)
    {
      	System.out.println("Main thread is: " + Thread.currentThread().getName());

        int[] numbers = {87, 52, 43, 67, 51, 16, 16, 62, 19, 28, 94, 80, 39, 77, 71, 52, 1, 94, 44, 50, 31, 82, 6, 30, 38, 42, 60, 15, 60, 1, 50, 87, 86, 22, 5, 4, 83, 49, 39, 9, 3, 44, 86, 29, 42, 67, 31, 74, 100, 75};

      	// Creating Thread
        SortArr s1 = new SortArr(numbers);

        s1.start();

        try {
            s1.join();
        } catch (InterruptedException e) {
            System.out.println("s1 message is: " + e.getMessage());
        }

        int[]res = s1.getResult();
        System.out.println("Main thread getResult is: " + res);
    }
}