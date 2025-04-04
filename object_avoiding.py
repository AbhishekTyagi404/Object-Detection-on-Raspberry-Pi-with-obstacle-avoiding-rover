import time
import RPi.GPIO as GPIO

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pins
TRIG = 26
ECHO = 16
MOTORS = {'left_f': 17, 'left_b': 27, 'right_f': 23, 'right_b': 24}
DISTANCE_THRESHOLD = 15  # cm
SLEEP_INTERVAL = 0.3     # seconds

def init_motors():
    for pin in MOTORS.values():
        GPIO.setup(pin, GPIO.OUT)

def set_motor_state(left_f, left_b, right_f, right_b):
    GPIO.output(MOTORS['left_f'], left_f)
    GPIO.output(MOTORS['left_b'], left_b)
    GPIO.output(MOTORS['right_f'], right_f)
    GPIO.output(MOTORS['right_b'], right_b)

def move_forward(): set_motor_state(True, False, True, False)
def move_left():    set_motor_state(True, False, False, False)
def move_right():   set_motor_state(False, False, True, False)
def move_back():    set_motor_state(False, True, False, True)
def stop():         set_motor_state(False, False, False, False)

# Ultrasonic Setup
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(2)

def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start, pulse_end = 0, 0

    timeout = time.time() + 0.04
    while GPIO.input(ECHO) == 0 and time.time() < timeout:
        pulse_start = time.time()

    timeout = time.time() + 0.04
    while GPIO.input(ECHO) == 1 and time.time() < timeout:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

def main():
    init_motors()
    print("🟢 Starting Object Avoidance Rover")

    try:
        while True:
            distance = measure_distance()
            timestamp = time.strftime("%H:%M:%S")
            print(f"[{timestamp}] Distance: {distance} cm")

            if distance >= DISTANCE_THRESHOLD:
                move_forward()
            else:
                stop()
                time.sleep(SLEEP_INTERVAL)
                command = input("Obstacle detected! Enter direction (left/right/back/kill): ").strip().lower()

                if command == 'left':
                    move_left()
                elif command == 'right':
                    move_right()
                elif command == 'back':
                    move_back()
                elif command == 'kill':
                    print("🛑 Stopping the rover.")
                    break
                else:
                    print("❗Invalid command. Use: left, right, back, kill.")
            
            time.sleep(SLEEP_INTERVAL)

    except KeyboardInterrupt:
        print("\n🔴 Interrupted by user.")

    finally:
        stop()
        GPIO.cleanup()
        print("GPIO cleaned up. Rover safely stopped.")

if __name__ == '__main__':
    main()
