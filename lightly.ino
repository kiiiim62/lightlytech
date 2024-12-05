Arduino: #include <SoftwareSerial.h>

#define HLW_RX_PIN 2

const float VOLTAGE_SCALING_FACTOR = 471.0 * 0.495 / (pow(2, 24) - 1);
const float CURRENT_SCALING_FACTOR = 30.9 / (0.001 * (pow(2, 24) - 1));
const float POWER_SCALING_FACTOR = VOLTAGE_SCALING_FACTOR * CURRENT_SCALING_FACTOR;

SoftwareSerial hlwSerial(HLW_RX_PIN, -1);

void setup() {
  Serial.begin(9600);
  hlwSerial.begin(4800);
  Serial.println("HLW8032 Energy Monitor Initialized");
}

void loop() {
  if (hlwSerial.available() >= 24) {
    uint8_t data[24];
    for (int i = 0; i < 24; i++) {
      data[i] = hlwSerial.read();
    }
    
    Serial.print("Raw Data: ");
    for (int i = 0; i < 24; i++) {
      if (data[i] < 0x10) Serial.print("0");
      Serial.print(data[i], HEX);
      Serial.print(" ");
    }
    Serial.println();
    
    uint8_t calculatedChecksum = 0;
    for (int i = 2; i < 23; i++) {
      calculatedChecksum += data[i];
    }
    calculatedChecksum %= 256;
    
    if (calculatedChecksum == data[23]) {
      uint32_t rawVoltage = (data[5] << 16) | (data[6] << 8) | data[7];
      uint32_t rawCurrent = (data[11] << 16) | (data[12] << 8) | data[13];
      uint32_t rawPower = (data[17] << 16) | (data[18] << 8) | data[19];
      
      float voltage = rawVoltage * VOLTAGE_SCALING_FACTOR;
      float current = rawCurrent * CURRENT_SCALING_FACTOR;
      float power = rawPower * POWER_SCALING_FACTOR;
      
      Serial.print("Voltage: ");
      Serial.print(voltage, 2);
      Serial.println(" V");
      
      Serial.print("Current: ");
      Serial.print(current, 2);
      Serial.println(" A");
      
      Serial.print("Power: ");
      Serial.print(power, 2);
      Serial.println(" W");
      
      Serial.println("------------------------");
    } else {
      Serial.println("Checksum Error!");
    }
  }
  
  delay(1000);
}