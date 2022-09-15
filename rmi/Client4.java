import java.util.Scanner;
import java.rmi.Naming;

public class Client4 {
    public static void main(String[] args) {
        Pessoa obj = null;
        Scanner myScanner = new Scanner(System.in);
        try { 
            String nome, sexo;
            double altura;
            
            obj = (Pessoa)Naming.lookup("//localhost/PessoaServer"); 
            
            System.out.println("Informe o nome: ");
            nome = myScanner.nextLine();
            System.out.println("Informe o sexo: ");
            sexo = myScanner.nextLine();
            System.out.println("Informe a altura: ");
            altura = myScanner.nextDouble();
           
            
            
            obj.setNome(nome);
            obj.setSexo(sexo);
            obj.setAltura(altura);

            
            
            System.out.println("Nome: "+obj.getNome());
            System.out.println("Sexo: "+obj.getSexo());
            System.out.println("Altura: "+obj.getAltura());
            System.out.print("Peso Ideal: ");
            System.out.printf("%.2f", obj.pesoIdeal());
            System.out.println("");
            
            
            myScanner.close();

        } catch (Exception e) { 
            System.out.println("Client exception: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
        
         
    }
}
