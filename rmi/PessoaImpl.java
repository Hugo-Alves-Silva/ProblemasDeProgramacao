import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class PessoaImpl extends UnicastRemoteObject implements Pessoa {
    private String nome, sexo;
    private double altura;

    public PessoaImpl() throws RemoteException {
        super();
    }
   
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setSexo(String sexo){
        this.sexo = sexo;
    }
    public void setAltura(double altura){
        this.altura = altura;
    }
    
    public String getNome(){
        return this.nome;
    }
    public String getSexo(){
        return this.sexo;
    }
    public double getAltura(){
        return this.altura;
    }
    
   public double pesoIdeal(){
        if(this.sexo.toLowerCase().equals("masculino"))
            return  (72.7 * this.altura) - 58;
        else
            return (62.1 * this.altura) - 44.7;
        
   }
    
    public static void main(String[] args) { 
        try { 
            Pessoa obj = new PessoaImpl();  
            Naming.rebind("//localhost/PessoaServer", obj); 
            System.out.println("PessoaServer bound in registry"); 
        } catch (Exception e) { 
            System.out.println("PessoaImpl err: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
    } 
}