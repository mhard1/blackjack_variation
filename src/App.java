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
        Integer trackedInt = null;
        int currCount = 0;
        int maxCount = 0;
        for (int i = 0; i < array.length; i++) {
            int currInt = array[i];
            if (null == trackedInt) {
                trackedInt = currInt;
                currCount = 1;
            } else {
                if (currInt == trackedInt) {
                    currCount++;
                } else {
                    if (currCount > maxCount) {
                        maxCount = currCount;
                        modeInts.clear();
                        modeInts.add(trackedInt);
                    } else if (currCount == maxCount) {
                        modeInts.add(trackedInt);
                    }

                    currCount = 1;
                    trackedInt = currInt;
                }
            }
        }

        for (Integer i : modeInts) {
            System.out.println(i);
        }
    }
}

