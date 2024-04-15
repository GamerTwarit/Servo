from gpiozero import AngularServo
import sys

def control_servo():
    # Setup the servo
    servo = AngularServo(15, min_pulse_width=0.0006, max_pulse_width=0.0023, min_angle=-90, max_angle=90)

    current_angle = 0  # Start at 0 degrees
    servo.angle = current_angle  # Initialize servo position

    print("Press Enter to increase the servo angle by 10°. Press any other key to reset to 0°.")

    while True:
        user_input = input()  # Wait for user input
        if user_input == "":
            current_angle += 10
            if current_angle > 90:
                current_angle = 90  # Ensure the angle does not go beyond 90 degrees
            servo.angle = current_angle
            print(f"Servo angle set to {current_angle}°")
        else:
            current_angle = 0  # Reset angle to zero on any other key press
            servo.angle = current_angle
            print("Servo angle reset to 0°.")

if __name__ == "__main__":
    try:
        control_servo()
    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        print("Servo reset to 0°.")
