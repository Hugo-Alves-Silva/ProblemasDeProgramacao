import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class MaioridadeImpl extends UnicastRemoteObject implements Maioridade {
    private String nome, sexo;
    private int idade;

    public MaioridadeImpl() throws RemoteException {
        super();
    }
    public void setNome(String nome){
        this.nome = nome;
    } 
    public void setSexo(String sexo){
        this.sexo = sexo;
    }
    public void setIdade(int idade){
        this.idade = idade;
    }
    
    public String getNome(){
        return this.nome;
    }
    public String getSexo(){
        return this.sexo;
    }
    public double getIdade(){
        return this.idade;
    }

    public boolean atingiuMaioridade(){
        if(this.sexo.toLowerCase().equals("Masculino")){
            if(this.idade >= 18) return true;
            else return false;
        }
        else{
            if(this.idade >= 21) return true;
            else return false;
        }
        
    }
    
    public static void main(String[] args) { 
        try { 
            Maioridade obj = new MaioridadeImpl(); 
            // Bind this object instance to the name "HelloServer" 
            Naming.rebind("//localhost/MaioridadeServer", obj); 
            System.out.println("MaioridadeServer bound in registry"); 
        } catch (Exception e) { 
            System.out.println("MaioridadeImpl err: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
    } 
}