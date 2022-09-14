import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class FuncionarioImpl extends UnicastRemoteObject implements Funcionario {
    private String nome, cargo;
    private double salario;

    public FuncionarioImpl() throws RemoteException {
        super();
    }
    public void setNome(String nome){
        this.nome = nome;
    } 
    public void setCargo(String cargo){
        this.cargo = cargo;
    }
    public void setSalario(double salario){
        this.salario = salario;
    }
    
    public String getNome(){
        return this.nome;
    }
    public String getCargo(){
        return this.cargo;
    }
    public double getSalario(){
        return this.salario;
    }

    public double reajuste(){
        if(this.cargo.toLowerCase().equals("programador") || this.cargo.toLowerCase().equals("programadora")){
            return this.salario * 0.18;
        }else if(this.cargo.toLowerCase().equals("operador") || this.cargo.toLowerCase().equals("operadora")){
            return this.salario * 0.2;
        }else{
            return 0.0;
        }

    }
    
    public static void main(String[] args) { 
        try { 
            Funcionario obj = new FuncionarioImpl(); 
            // Bind this object instance to the name "HelloServer" 
            Naming.rebind("//localhost/ReajusteServer", obj); 
            System.out.println("ReajusteServer bound in registry"); 
        } catch (Exception e) { 
            System.out.println("FuncionarioImpl err: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
    } 
}