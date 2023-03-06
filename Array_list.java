import java.util.ArrayList;
import java.util.Collections;

public class Array_list
{
    public static void main(String[] args)
        {
            ArrayList<Integer> list1 = new ArrayList<Integer>();

            // append operation

            list1.add(1);
            list1.add(2);
            list1.add(3);
            list1.add(4);
            
            System.out.println(list1);

            // accessing patilcular element at index
            System.out.println(list1.get(3)); // by index

            // append at location
            list1.add(2,5); // index , element
            System.out.println(list1);

            list1.set(0, 7);
            System.out.println(list1);

            // remove element
            // list1.remove(0); // by index
            list1.remove(1);
            System.out.println(list1);

            // size of array
            int length = list1.size();
            System.out.println(length+"\n");

            list1.add(0);
            list1.add(1);

            // iteration 
            for(int i =0;i<list1.size();i++)
            {
                System.out.println(list1.get(i));
            }
            System.out.println(list1);

            Collections.sort(list1);
            System.out.println(list1);

            
        }
}