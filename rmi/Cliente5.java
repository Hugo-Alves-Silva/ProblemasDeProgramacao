import java.util.Scanner;
import java.rmi.Naming;

public class Cliente5 {
    public static void main(String[] args) {
        Nadador obj = null;
        Scanner myScanner = new Scanner(System.in);
        try { 
            int idade;
            obj = (Nadador)Naming.lookup("//localhost/NadadorServer"); 
            
            System.out.println("Informe a idade: ");
            idade = myScanner.nextInt();
            
           
            
            
            obj.setIdade(idade);
            

            
            
            System.out.println("Categoria: "+obj.getCategoria());
            
            
            myScanner.close();

        } catch (Exception e) { 
            System.out.println("Client exception: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
        
         
    }
}
