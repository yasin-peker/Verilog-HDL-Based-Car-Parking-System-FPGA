# Verilog-HDL-Based-Car-Parking-System-FPGA
Welcome to the Car Parking System repository, featuring an innovative and efficient Verilog HDL implementation of a smart car parking system running on an FPGA. This advanced parking system provides a seamless and secure experience for car owners, offering password-based access control, LED-based traffic light indicators, and 7-Segment displays to show real-time status messages.

# Key Features
- **Secure Access Control:** The Car Parking System allows registered users to enter the car park by entering their personalized passwords. Unauthorized access is strictly prohibited, ensuring enhanced security and peace of mind.

- **Real-Time Finite State Machine (FSM):** The core functionality of the system is built on a sophisticated Moore Finite State Machine (FSM) that effectively manages various states to regulate car park entry and exit.

- **Intuitive LED Traffic Lights:** The FPGA-controlled LED-based traffic light system ensures clear and intuitive visual cues for drivers. A green light signifies successful entry or presence inside the car park, while a red light indicates an incorrect password or the car park being full.

- **Informative 7-Segment Displays:** The 7-Segment displays provide real-time feedback to users, showcasing meaningful status messages. Whether it's "Entering Password (EP)," "Wrong Password (W)," "Correct Password (CP)," or "Waiting for Next Car (SP)," users can stay informed at all times.

# Testbench using Cocotb
The Car Parking System comes with a robust and comprehensive testbench code developed using Cocotb, a powerful framework for testing Verilog designs. The testbench thoroughly validates the functionality of the Car Parking System under various scenarios, including correct and incorrect password inputs, sensor activations, state transitions, LED and 7-Segment display updates, and more.

The Cocotb testbench provides valuable insights into the system's behavior, ensuring its reliability, accuracy, and compliance with specifications. It enables developers to detect and fix potential bugs early in the development process, leading to a more robust and reliable final implementation.

The testbench code, written by Süleyman Yasin Peker, exemplifies the verification process of the Car Parking System. It covers two distinct test cases, simulating different user interactions and system responses to ensure its correct operation. The tests involve setting inputs for sensors and password verification, and the testbench monitors the output states, LED indicators, and 7-Segment display outputs.  

# How it Works
The Car Parking System is designed as a Moore Finite State Machine (FSM) with five states that govern the car park's functionality:

- **IDLE_STATE:** In the initial state, the system waits for sensor inputs, keeping an eye on the entrance sensor for any activity.

- **PASSWORD_WAITING_STATE:** Upon detecting activation of the entrance sensor, the system transitions to this state, waiting for the user to input the correct password.

- **WRONG_PASSWORD_STATE:** If the entered password is incorrect, the FSM moves to this state, notifying the user of the invalid attempt and giving them the chance to re-enter the correct password.

- **CORRECT_PASSWORD_STATE:** When the user enters the correct password, the FSM moves to this state, granting access to the car park. The system dynamically checks sensor states to decide whether a new car is waiting to enter or if the current user is exiting the car park.

- **WAIT_STATE:** In this state, the system awaits the next car at the entrance to input their password. If the correct password is entered, the FSM transitions back to the CORRECT_PASSWORD_STATE, ready for the next car to enter.

# State Transitions
The FSM transitions between states based on the following conditions:
- In IDLE_STATE, if the entrance sensor is activated, it moves to PASSWORD_WAITING_STATE.
- In PASSWORD_WAITING_STATE, the system waits for the user to enter the correct password. If the user fails to enter the correct password after a certain time (3 clock cycles), it moves to WRONG_PASSWORD_STATE.
- In WRONG_PASSWORD_STATE, the system continues to check the entered password. If the user eventually enters the correct password, it moves to CORRECT_PASSWORD_STATE; otherwise, it stays in WRONG_PASSWORD_STATE.
- In CORRECT_PASSWORD_STATE, the system checks the sensors to determine the next state. If both entrance and exit sensors are activated, it moves to WAIT_STATE. If only the exit sensor is activated, the user is considered to have successfully entered the car park, and the system moves back to IDLE_STATE. If only the entrance sensor is activated, it stays in CORRECT_PASSWORD_STATE to wait for the user to check out.
- In WAIT_STATE, the system waits for the new user at the entrance to enter their password. If the correct password is entered, it moves back to CORRECT_PASSWORD_STATE; otherwise, it stays in WAIT_STATE.

# LED and 7-Segment Displays

The Car Parking System leverages LEDs and 7-Segment displays to provide visual feedback and convey essential system status:

- **Green Light:** Illuminates when the entered password is correct, indicating that the car can enter the car park or is already parked inside.

- **Red Light:** Turns on when an incorrect password is entered or the car park is at maximum capacity, indicating that access is denied.

- **7-Segment Displays:** Show real-time status messages to keep users informed. Display messages like "Entering Password (EP)," "Wrong Password (W)," "Correct Password (CP)," and "Waiting for Next Car (SP)."

# Getting Started
1. Clone this repository to your local machine.
2. Open the Verilog HDL code in your preferred FPGA development environment.
3. Synthesize and implement the code on your FPGA board.

# Compatibility
The code is written in Verilog HDL and is intended to run on FPGA platforms. Please refer to your FPGA board documentation for specific implementation instructions.

# Credits
This project was created by Süleyman Yasin Peker as a part of Intelligent Decision Mechanism Research.


