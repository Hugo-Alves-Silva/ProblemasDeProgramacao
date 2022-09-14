import java.util.Scanner;
import java.rmi.Naming;

public class Client2 {
    public static void main(String[] args) {
        Maioridade obj = null;
        Scanner myScanner = new Scanner(System.in);
        try { 
            String nome, sexo;
            int idade;
            
            obj = (Maioridade)Naming.lookup("//localhost/MaioridadeServer"); 
            
            System.out.println("Informe o nome: ");
            nome = myScanner.nextLine();
            System.out.println("Informe o sexo: ");
            sexo = myScanner.nextLine();
            System.out.println("Informe a idade: ");
            idade = myScanner.nextInt();
            
            obj.setNome(nome);
            obj.setSexo(sexo);
            obj.setIdade(idade);
            
            
            
            System.out.println("Nome: "+obj.getNome());
            System.out.println("Sexo: "+obj.getSexo());
            System.out.println("Idade "+obj.getIdade());
            if(obj.atingiuMaioridade()){
                System.out.println("Atintgiu a maioridade!");
            }else{
                System.out.println("Não atintgiu a maioridade.");
            }
            myScanner.close();

        } catch (Exception e) { 
            System.out.println("Client exception: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
        
         
    }
}
