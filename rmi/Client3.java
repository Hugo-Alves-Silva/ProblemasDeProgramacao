import java.util.Scanner;
import java.rmi.Naming;

public class Client3 {
    public static void main(String[] args) {
        Aluno obj = null;
        Scanner myScanner = new Scanner(System.in);
        try { 
            String nome;
            double n1, n2, n3;
            
            obj = (Aluno)Naming.lookup("//localhost/AlunoServer"); 
            
            System.out.println("Informe o nome: ");
            nome = myScanner.nextLine();
            System.out.println("Informe as notas n1, n2 e n3: ");
            n1 = myScanner.nextDouble();
            n2 = myScanner.nextDouble();
            n3 = myScanner.nextDouble();
           
            
            
            obj.setNome(nome);
            obj.setNotas(n1, n2, n3);
            

            
            
            System.out.println("Nome: "+obj.getNome());
            if(obj.aprovado())
                System.out.println("Aprovado!");
            else
                System.out.println("Reprovado.");
            
          
            
            
            myScanner.close();

        } catch (Exception e) { 
            System.out.println("Client exception: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
        
         
    }
}
