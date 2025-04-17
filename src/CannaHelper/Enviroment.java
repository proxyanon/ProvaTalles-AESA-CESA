package CannaHelper;

class Environment {
    private double temperature;
    private double humidity;
    private int lightHours;
    private String growingMethod;
    private double airflow;
    private boolean isPestPresent;
    private String lightType;

    public Environment(double temperature, double humidity, int lightHours, String growingMethod,
                       double airflow, boolean isPestPresent, String lightType) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.lightHours = lightHours;
        this.growingMethod = growingMethod;
        this.airflow = airflow;
        this.isPestPresent = isPestPresent;
        this.lightType = lightType;
    }

    public String getInfo() {
        return "Temperatura (°C): " + temperature +
                ", Umidade (%): " + humidity +
                ", Horas de luz: " + lightHours +
                ", Método de cultivo: " + growingMethod +
                ", Fluxo de ar: " + airflow +6 +
                ", Presença de pragas: " + (isPestPresent ? "Sim" : "Não") +
                ", Tipo de luz: " + lightType;
    }

    public String recommendLightCycle(int plantStage) {
        switch (plantStage) {
            case 1:
                return "Recomendação para Germinação/Muda: 18-24 horas de luz, 0-6 horas de escuridão.";
            case 2:
                return "Recomendação para Vegetativo: 18 horas de luz, 6 horas de escuridão.";
            case 3:
                return "Recomendação para Floração: 12 horas de luz, 12 horas de escuridão.";
            default:
                return "Estágio desconhecido.";
        }
    }
    
    public double getCurrentHumidity() {
        return humidity;
    }
}
