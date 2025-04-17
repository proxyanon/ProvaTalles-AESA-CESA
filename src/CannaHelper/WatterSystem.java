package CannaHelper;

class WaterSystem {
    private double waterAmount;
    private int wateringFrequency;
    private double waterTemperature;
    private boolean isFiltered;
    private boolean hasRunoff;
    private double tdsLevel;
    private String irrigationMethod;

    public WaterSystem(double waterAmount, int wateringFrequency, double waterTemperature,
                       boolean isFiltered, boolean hasRunoff, double tdsLevel, String irrigationMethod) {
        this.waterAmount = waterAmount;
        this.wateringFrequency = wateringFrequency;
        this.waterTemperature = waterTemperature;
        this.isFiltered = isFiltered;
        this.hasRunoff = hasRunoff;
        this.tdsLevel = tdsLevel;
        this.irrigationMethod = irrigationMethod;
    }

    public String getInfo() {
        return "Quantidade de água (L): " + waterAmount +
                ", Frequência de rega (dias): " + wateringFrequency +
                ", Temperatura da água (°C): " + waterTemperature +
                ", Água filtrada: " + (isFiltered ? "Sim" : "Não") +
                ", Com escoamento: " + (hasRunoff ? "Sim" : "Não") +
                ", Nível TDS: " + tdsLevel +
                ", Método de irrigação: " + irrigationMethod;
    }

    public String checkWateringNeeds(double plantHeight, double humidity) {
        if (humidity < 40 && plantHeight > 30) {
            return "Aumente a frequência de rega.";
        } else if (humidity > 70) {
            return "Diminua a frequência de rega para evitar problemas de fungos.";
        } else {
            return "Frequência de rega adequada.";
        }
    }
}