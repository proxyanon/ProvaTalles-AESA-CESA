/**
 *
 * @author Daniel Victor Freire 2º perído projeto POO {@link https://github.com/proxyanon/ProvaTalles.java}
 * @version 0.0.1
 * @since 0.0.1
 * @acess public
 * @file Plant.java
 * @pacakge CannaHelper
 * @description - Classe responsável por definir os parametrôs da planta e genetica que vai ser cultivada
 * @see {@link:https://github.com/proxyanon/ProvaTalles.java}
 */

// Package declaration
package CannaHelper;

import java.util.ArrayList;
import java.util.Arrays;
import CannaHelper.*;

class Plant {

    // Deifine atributos da class Plant
    private String strain;
    private int growthStage;
    private double height;
    private double phLevel;
    private boolean isHealthy;
    private int daysOld;
    private String geneticOrigin;

    public Plant(String strain, int growthStage, double height, double phLevel,
                 boolean isHealthy, int daysOld, String geneticOrigin) {
        this.strain = strain;
        this.growthStage = growthStage;
        this.height = height;
        this.phLevel = phLevel;
        this.isHealthy = isHealthy;
        this.daysOld = daysOld;
        this.geneticOrigin = geneticOrigin;
    }

    public String getInfo() {
        return "Strain: " + strain +
                ", Estágio de crescimento: " + growthStage +
                ", Altura (cm): " + height +
                ", pH: " + phLevel +
                ", Saudável: " + (isHealthy ? "Sim" : "Não") +
                ", Idade (dias): " + daysOld +
                ", Origem genética: " + geneticOrigin;
    }

    public String checkPhLevel() {
        if (phLevel < 5.5) {
            return "pH muito ácido. Recomendação: Aumentar o pH.";
        } else if (phLevel >= 5.5 && phLevel <= 6.5) {
            return "pH ideal para cannabis.";
        } else {
            return "pH muito alcalino. Recomendação: Diminuir o pH.";
        }
    }

    public void updateGrowthStage() {
        if (daysOld < 21) {
            growthStage = 1; // Germinação/Muda
        } else if (daysOld < 60) {
            growthStage = 2; // Vegetativo
        } else {
            growthStage = 3; // Floração
        }
    }

    // Métodos para acessar alguns dados internos sem usar getters tradicionais
    public int getCurrentGrowthStage() {
        return growthStage;
    }

    public double getCurrentHeight() {
        return height;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Plant other = (Plant) obj;
        return strain.equals(other.strain) &&
                growthStage == other.growthStage &&
                Double.compare(height, other.height) == 0 &&
                Double.compare(phLevel, other.phLevel) == 0 &&
                isHealthy == other.isHealthy &&
                daysOld == other.daysOld &&
                geneticOrigin.equals(other.geneticOrigin);
    }
}