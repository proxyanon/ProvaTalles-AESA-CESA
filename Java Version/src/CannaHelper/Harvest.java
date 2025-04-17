package CannaHelper;

class Harvest {
    private int floweringWeeks;
    private boolean trichomesReady;
    private double estimatedYield;
    private String curingMethod;
    private int dryingDays;
    private int curingWeeks;
    private String harvestTechnique;

    public Harvest(int floweringWeeks, boolean trichomesReady, double estimatedYield,
                   String curingMethod, int dryingDays, int curingWeeks, String harvestTechnique) {
        this.floweringWeeks = floweringWeeks;
        this.trichomesReady = trichomesReady;
        this.estimatedYield = estimatedYield;
        this.curingMethod = curingMethod;
        this.dryingDays = dryingDays;
        this.curingWeeks = curingWeeks;
        this.harvestTechnique = harvestTechnique;
    }

    public String getInfo() {
        return "Semanas de floração: " + floweringWeeks +
                ", Tricomas prontos: " + (trichomesReady ? "Sim" : "Não") +
                ", Rendimento estimado (g): " + estimatedYield +
                ", Método de cura: " + curingMethod +
                ", Dias de secagem: " + dryingDays +
                ", Semanas de cura: " + curingWeeks +
                ", Técnica de colheita: " + harvestTechnique;
    }

    public String checkHarvestReadiness() {
        if (floweringWeeks < 6) {
            return "Muito cedo para colher.";
        } else if (floweringWeeks >= 6 && floweringWeeks <= 9) {
            if (trichomesReady) {
                return "Pronto para colheita.";
            } else {
                return "Verifique os tricomas para confirmar a maturidade.";
            }
        } else {
            return "Pode estar maduro demais. Verifique os tricomas para determinar.";
        }
    }
}