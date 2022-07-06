import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {


        File file = new File(
                "course.txt");


        BufferedReader br
                = null;
        try {
            br = new BufferedReader(new FileReader(file));
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

        String st;

        while (true)


        {
            try {
                if (!((st = br.readLine()) != null)) break;
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
//            System.out.println(st);
            String[] courseDetails=st.split("\n ");

            for (int i=0 ;i< courseDetails.length; i++){
                String [] course=courseDetails[i].split(" ");
               String[] newarr= Arrays.copyOfRange(course, 2, course.length);

               System.out.println();


                System.out.println("Course code = "+course[0] +" Credit Hours = "+course[1]+" Course Title = " +newarr[0]+" " +newarr[1]+" " +newarr[2]+" " +newarr[3]+" " +newarr[4]);
            }
        }

    }
}