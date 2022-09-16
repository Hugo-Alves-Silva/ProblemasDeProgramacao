import java.util.Scanner;
import java.rmi.Naming;

public class Client8 {
    public static void main(String[] args) {
        Saldo obj = null;
        Scanner myScanner = new Scanner(System.in);
        try { 
            double saldo;
            obj = (Saldo)Naming.lookup("//localhost/SaldoServer"); 
            
            System.out.println("Informe o saldo médio: ");
            saldo = myScanner.nextDouble();
            
           
            
            
            obj.setSaldoMedio(saldo);
            

            
            System.out.println("Saldo médio: "+saldo);
            System.out.println("Crédito: "+obj.getCredito());
            
            
            myScanner.close();

        } catch (Exception e) { 
            System.out.println("Client exception: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
        
         
    }
}
