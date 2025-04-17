package CannaHelper;

class Nutrition {
    private double nitrogen;
    private double phosphorus;
    private double potassium;
    private double calcium;
    private double magnesium;
    private double iron;
    private String fertilizer;

    public Nutrition(double nitrogen, double phosphorus, double potassium, double calcium,
                     double magnesium, double iron, String fertilizer) {
        this.nitrogen = nitrogen;
        this.phosphorus = phosphorus;
        this.potassium = potassium;
        this.calcium = calcium;
        this.magnesium = magnesium;
        this.iron = iron;
        this.fertilizer = fertilizer;
    }

    public String getInfo() {
        return "Nitrogênio (N): " + nitrogen +
                ", Fósforo (P): " + phosphorus +
                ", Potássio (K): " + potassium +
                ", Cálcio (Ca): " + calcium +
                ", Magnésio (Mg): " + magnesium +
                ", Ferro (Fe): " + iron +
                ", Fertilizante: " + fertilizer;
    }

    public String recommendNutrients(int growthStage) {
        if (growthStage == 1) {
            return "Para mudas: baixo N, baixo P, baixo K.";
        } else if (growthStage == 2) {
            return "Para crescimento vegetativo: alto N, médio P, médio K.";
        } else if (growthStage == 3) {
            return "Para floração: baixo N, alto P, alto K.";
        } else {
            return "Estágio desconhecido.";
        }
    }
}
