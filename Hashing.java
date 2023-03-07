import java.util.HashSet;
import java.util.Iterator;

public class Hashing
{
    public static void main(String[] args) 
    {
        HashSet<Integer> set1 = new HashSet<Integer>(); 

        set1.add(1);
        set1.add(2);
        set1.add(3);
        set1.add(4);
        set1.add(1);
        set1.add(5);
        System.out.println(set1.contains(1));
        set1.remove(1);
        System.out.println(set1.contains(1));
        System.out.println(set1);
        System.out.println("size of set1 is "+set1.size());

        Iterator it = set1.iterator();
        
        // for(int i = 0;i<set1.size();i++)
        // {
        //     System.out.println(it.next()+" "+it.hasNext());
        // }

        while(it.hasNext())
        {
            System.out.println(it.next());
        }
        
    }
}