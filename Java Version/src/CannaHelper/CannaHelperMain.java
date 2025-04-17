/**
 *
 * @author Daniel Victor Freire 2º perído projeto POO {@link https://github.com/proxyanon/ProvaTalles.java}
 * @version 0.0.1
 * @since 0.0.1
 * @acess public
 * @file src\CannaHelper\CannaHelperMain.java
 * @filenmae CannaHelperMain.javas
 * @pacakge CannaHelper
 * @description - Classe principal do sistmea resoonsável por instânciar classes e interagir com o usuarios também fazendo tambémm algumas validações pedidas no projeto como uso de switch
 * @see {@link:https://github.com/proxyanon/ProvaTalles.java}
 */

package CannaHelper;

import java.util.ArrayList;
import java.util.Scanner;

class CannaHelperMain {

    public static void main(String[] args) {

        /**
         * @class Scanner {scanner} - Instância do scannaer pra letirua do System.in
         */
        Scanner scanner = new Scanner(System.in);

        // Array com nomes das classes
        String[] classNames = {"Plant", "Environment", "Nutrition", "WaterSystem", "Harvest"}; // Isso ficou porco e horrível perdão poderia atuamtizar esse processo

        // Print not std.out a mensagem abaixo
        System.out.println("Bem-vindo ao CannaHelper - Assistente para Cultivo de Cannabis Medicinal");
        System.out.println("--------------------------------------------------------------");
        System.out.println("\nClasses disponíveis no sistema:");

        // Tem esse for padrão e tem a alternativa abaixo
        /*for (int i = 0; i < classNames.length; i++) {
            System.out.println((i+1) + ". " + classNames[i]);
        }*/

        int index_classnames = 1; // Index da Array porca de classname

        // Percorrendo a Array porca e preguiçosa contendo aa lista de classes e mostra no std.out o nome das classes
        for(String c: classNames){
            System.out.println("["+index_classnames+"] -> " + c);
            index_classnames += 1;
        }

        // Criando instâncias das classes com paramêtros dinâmicos
        Plant plant = new Plant("Critical Mass CBD", 2, 45.5, 6.2, true, 35, "Indica dominante");
        Environment environment = new Environment(24.5, 55.0, 18, "Indoor - Solo", 3.5, false, "LED Full Spectrum");
        Nutrition nutrition = new Nutrition(4.5, 3.2, 3.8, 2.1, 1.5, 0.5, "BioBizz Organic");
        WaterSystem waterSystem = new WaterSystem(2.5, 2, 22.0, true, true, 350.0, "Rega manual");
        Harvest harvest = new Harvest(7, false, 120.0, "Potes de vidro", 10, 4, "Colheita parcial");

        // Com o scanner é recolhido o std.in dado pelo usuário que vai executar um ação sei que não foi pedido porém achei interessante aplicar
        System.out.println("\nEscolha uma opção para obter informações:");
        System.out.println("1. Informações da planta");
        System.out.println("2. Informações do ambiente");
        System.out.println("3. Informações de nutrição");
        System.out.println("4. Informações do sistema de água");
        System.out.println("5. Informações da colheita");
        System.out.print("Digite sua escolha (1-5): ");

        int choice = scanner.nextInt();

        // Validação requerida usando switch
        switch (choice) {
            case 1:
                System.out.println("\nInformações da planta:");
                System.out.println(plant.getInfo());
                System.out.println(plant.checkPhLevel());
                break;
            case 2:
                System.out.println("\nInformações do ambiente:");
                System.out.println(environment.getInfo());
                // Correção: Usando o método que criamos para acessar o estágio de crescimento
                System.out.println(environment.recommendLightCycle(plant.getCurrentGrowthStage()));
                break;
            case 3:
                System.out.println("\nInformações de nutrição:");
                System.out.println(nutrition.getInfo());
                System.out.println(nutrition.recommendNutrients(plant.getCurrentGrowthStage()));
                break;
            case 4:
                System.out.println("\nInformações do sistema de água:");
                System.out.println(waterSystem.getInfo());
                // Correção: Usando os métodos que criamos para acessar altura e umidade
                System.out.println(waterSystem.checkWateringNeeds(plant.getCurrentHeight(),
                        environment.getCurrentHumidity()));
                break;
            case 5:
                System.out.println("\nInformações da colheita:");
                System.out.println(harvest.getInfo());
                System.out.println(harvest.checkHarvestReadiness());
                break;
            default:
                System.out.println("Opção inválida.");
        }

        // Criando e manipulando um ArrayList
        System.out.println("\nDemonstrando operações com ArrayList de plantas:");
        ArrayList<Plant> plantCollection = new ArrayList<>();

        // Adicionando plantas à coleção
        plantCollection.add(plant);
        plantCollection.add(new Plant("Charlotte's Web", 3, 65.0, 6.0, true, 75, "Sativa dominante"));
        plantCollection.add(new Plant("Harlequin", 1, 15.0, 5.8, true, 14, "Híbrida 75/25"));

        // Demonstrando método contains (adicionamos o método equals na classe Plant)
        Plant searchPlant = new Plant("Critical Mass CBD", 2, 45.5, 6.2, true, 35, "Indica dominante");
        System.out.println("A coleção contém Critical Mass CBD? " +
                (plantCollection.contains(searchPlant) ? "Sim" : "Não"));

        // Imprimindo todas as plantas da coleção
        System.out.println("\nPlantas na coleção:");
        for (Plant p : plantCollection) {
            System.out.println("- " + p.getInfo());
        }

        // Removendo uma planta e imprimindo a coleção novamente
        System.out.println("\nRemovendo a segunda planta da coleção...");
        plantCollection.remove(1);

        System.out.println("Plantas na coleção após remoção:");
        for (Plant p : plantCollection) {
            System.out.println("- " + p.getInfo());
        }

        scanner.close();
    }
}