import time
import RPi.GPIO as GPIO

# GPIO pin configuration
GAS_SENSOR_PIN = 17
BUZZER_PIN = 27
LED_PIN = 22

# Most MQ sensor modules make DO LOW when gas is detected
GAS_DETECTED_STATE = GPIO.LOW

GPIO.setmode(GPIO.BCM)

GPIO.setup(
    GAS_SENSOR_PIN,
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP
)

GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

print("Gas leakage detector started.")
print("Allow the sensor to warm up...")
time.sleep(30)

try:
    while True:
        gas_status = GPIO.input(GAS_SENSOR_PIN)

        if gas_status == GAS_DETECTED_STATE:
            print("WARNING: Gas leakage detected!")

            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            GPIO.output(LED_PIN, GPIO.HIGH)

        else:
            print("Air is normal.")

            GPIO.output(BUZZER_PIN, GPIO.LOW)
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping gas leakage detector...")

finally:
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
