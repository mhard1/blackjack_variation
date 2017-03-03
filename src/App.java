import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Ninj0r
 */
public class App {
    public static void main(String[] args) {
        Integer[] array = new Integer[]{1,2,3,4,5,5,5,6,7,7,7,9,9};
        List<Integer> modeInts = new ArrayList<>();
        int trackedInt = array[0];
        int trackedCount = 1;
        int maxCount = 0;
        for (int i = 1; i < array.length; i++) {
            int currInt = array[i];
            if (currInt == trackedInt) {
                trackedCount++;
            } else {
                if (trackedCount > maxCount) {
                    maxCount = trackedCount;
                    modeInts.clear();
                    modeInts.add(trackedInt);
                } else if (trackedCount == maxCount) {
                    modeInts.add(trackedInt);
                }

                trackedCount = 1;
                trackedInt = currInt;
            }
        }

        for (Integer i : modeInts) {
            System.out.println(i);
        }
    }
}
