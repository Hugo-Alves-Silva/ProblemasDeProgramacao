import java.util.Scanner;
import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        Funcionario obj = null;        
        Scanner myScanner = new Scanner(System.in);
        try { 
            String nome, cargo;
            double salario, reajuste;
            
            obj = (Funcionario)Naming.lookup("//localhost/ReajusteServer"); 
            
            System.out.println("Informe o nome: ");
            nome = myScanner.nextLine();
            System.out.println("Informe o cargo: ");
            cargo = myScanner.nextLine();
            System.out.println("Informe o salário: ");
            salario = myScanner.nextDouble();
            
            obj.setNome(nome);
            obj.setCargo(cargo);
            obj.setSalario(salario);
            
            reajuste = obj.reajuste();
            obj.setSalario(salario + reajuste);
            
            System.out.println("Nome: "+obj.getNome());
            System.out.println("Cargo: "+obj.getCargo());
            System.out.println("Novo salário "+obj.getSalario());
            myScanner.close();

        } catch (Exception e) { 
            System.out.println("Client exception: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
        
         
    }
}
