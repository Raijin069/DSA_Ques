import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;


public class file_handling_java
{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        
        // file creation in java
        File my_file = new File("st_detail.txt");
        try
            {
                my_file.createNewFile();
            }
        catch(Exception e)
            {
                System.out.println("unable to create this file");
                System.out.println(e);
            }


            System.out.println("Enter the first name");
            String first_name = sc.next();

            System.out.println("Enter the last name");
            String last_name = sc.next();

            System.out.println("Enter the roll no");
            int roll_no = sc.nextInt();

            System.out.println("Enter the age");
            int age = sc.nextInt();

            System.out.println("Enter the branch name");
            String branch_name = sc.next();


        try
            {
                FileWriter fileWriter = new FileWriter("st_detail.txt");
                String detail1 = "name: "+first_name+ " " + last_name + "\n";
                String detail2 = "roll no: "+roll_no+ "\nage: " + age + "\nbranch: " + branch_name;
                String comp_detail = detail1+detail2;

                fileWriter.write(comp_detail);
                fileWriter.close();
            }
        catch(Exception e)
            {   
                System.out.println(e);
            }

        try
            {
                System.out.println();
                // reading 
                System.out.println("enter 1 to read or 2 to delete");
                int choice = sc.nextInt();

                if (choice == 1){
                Scanner rd = new Scanner(my_file);
                
                System.out.println("printing details: \n");
                while(rd.hasNextLine())
                {
                    String line = rd.nextLine();
                    System.out.println(line);
                }
                // System.out.println("enter a to print detail else anything to delete");
                rd.close();
            }
            else if(choice==2)
            {
                if(my_file.delete())
                {
                    System.out.println("deleted file");
                }
            }
            else
            {
                System.out.println("enter 1 or 2 only");
            }
            
            
        }
        catch(Exception e)
            {
                System.out.println(e+"error hai isme");
            }        

    }
}