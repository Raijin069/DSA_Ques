import java.util.HashMap;

public class Hash_Map {
    public static void main(String[] args)
    {
        HashMap<String,Integer> h1 = new HashMap<>();
        System.out.print(h1.isEmpty());
        h1.put("aseem", 57);
        h1.put("sreeraj", 73);
        h1.put("manish", 75);
        System.out.println(h1);
        h1.put("aseem", 64);
        System.out.println(h1);

        System.out.println(h1.keySet());
        System.out.println(h1.values());
        System.out.println(h1.size());
    }
    
}
