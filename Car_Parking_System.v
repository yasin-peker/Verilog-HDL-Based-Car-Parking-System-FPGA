module Car_Parking_System(

	input clk, reset,
	// There are two sensors at the entrance and the exit of the car park
	input entrance_sensor, exit_sensor,
	// Passwords of the registered users 
	input [1:0] password_user1, password_user2,
	// Traffic light colors of the car parking system represented by green and red LEDs
	output wire green_light, red_light,
	// 7-Segment display outputs
	output reg [6:0] hex1, hex2

);

	/* Parameterize the states of the Moore Finite State Machine (FSM)
	 In the Moore FSM, output only depends on the current state
	 There are 5 states of the FSM. These are the states:
	 - IDLE_STATE: Initial state of the system that waits sensor inputs
	 - PASSWORD_WAITING_STATE: When the entrance sensor is activated
	 - WRONG_PASSWORD_STATE: If the entered password of the user is wrong
	 - CORRECT_PASSWORD_STATE: If the entered password of the user is correct
	 - WAIT_STATE: If the entrance and the exit sensors are actived at the same time
	*/
	
	parameter IDLE_STATE = 3'b000, 
				 PASSWORD_WAITING_STATE = 3'b001, 
				 WRONG_PASSWORD_STATE = 3'b010, 
				 CORRECT_PASSWORD_STATE = 3'b011,
				 WAIT_STATE = 3'b100;
	
	// Define current and next state registers, temporary registers and counter.
	reg [2:0] current_state, next_state;
	reg [31:0] counter;
	reg green_light_tmp, red_light_tmp;
	
	// Assign Next State according to the reset signal and clock.
	always @(posedge clk or negedge reset)
	begin
	
		if(~reset)
			current_state = IDLE_STATE;
		
		else
			current_state = next_state;
			
	end
	
	
	// Start counter if the current state is PASSWORD_WAITING_STATE.
	// Otherwise, clear the counter.
	always @(posedge clk or negedge reset)
	begin
	
		if(~reset)
			counter <= 0;
			
		// If password is being waited, increment the counter by 1.
		else if(current_state == PASSWORD_WAITING_STATE)
			counter <= counter + 1;
	
		else
			counter <= 0;
			
	end
	
	// FSM Implementation
	always @(*)
	begin
	
		case(current_state)
		IDLE_STATE: 
		begin
		
			// Check the entrance sensor. If it is actived, then enter the PASSWORD_WAITING_STATE.
			if (entrance_sensor == 1)
				next_state = PASSWORD_WAITING_STATE;
				
			else
				next_state = IDLE_STATE;
		end
		
		PASSWORD_WAITING_STATE:
		begin
		
			// If the counter is less than or equalt to 3, continue waiting the password.
			if (counter <= 3)
				next_state = PASSWORD_WAITING_STATE;
			
			// After waiting enough time, check whether the passwords entered are correct or not.
			else
			begin
				
				if((password_user1 == 2'b01) && (password_user2 == 2'b11))
					next_state = CORRECT_PASSWORD_STATE;
					
				else
					next_state = WRONG_PASSWORD_STATE;
				
			end
			
		end
		
		// Check the password again, if it is entered wrong, stay in the WRONG_PASSWORD_STATE.
		WRONG_PASSWORD_STATE:
		begin
			
			if((password_user1 == 2'b01) && (password_user2 == 2'b11))
				next_state = CORRECT_PASSWORD_STATE;
			
			else
				next_state = WRONG_PASSWORD_STATE;
		
		end
		
		// If the password entered is correct, then check the sensors. If both entrance and the exit
		// sensors are actived, then enter the WAIT_STATE. This is because of the fact that there is 
		// a new car is at the entrance of the car parking system, and the new user should enter the password
		// to get inside of the car park.
		CORRECT_PASSWORD_STATE:
		begin
			
			// The previous car is exiting and a new car is at the entrance of the parking system.
			if(entrance_sensor == 1 && exit_sensor == 1)
				next_state = WAIT_STATE;
			
			// The user is successfully entered the car parking system. So, new users are waited in the IDLE_STATE.
			else if(exit_sensor == 1)
				next_state = IDLE_STATE;
			
			// The user has not checked out of the parking system. So, wait for the user to activate the exit sensor.
			else
				next_state = CORRECT_PASSWORD_STATE;
		end
		
		WAIT_STATE:
		begin
		
			// Check again passwords of the new user at the entrance of the car parking system.
			if((password_user1 == 2'b01) && (password_user2 == 2'b11))
				next_state = CORRECT_PASSWORD_STATE;
			
			else
				next_state = WAIT_STATE;
		
		end
		
		// By default, the system should be in the IDLE_STATE
		default: next_state = IDLE_STATE;
		
		endcase
	
	end
	
	// Assign LED colors and the 7-segment display outputs
	always @(posedge clk)
	begin

		case(current_state)
		
		IDLE_STATE:
		begin
			
			// In the IDLE_STATE, both of the LEDs are off
			green_light_tmp = 1'b0;
			red_light_tmp = 1'b0;
			
			// 7-segment displays are off
			hex1 = 7'b111_1111;
			hex2 = 7'b111_1111;
		
		end
		
		PASSWORD_WAITING_STATE:
		begin
		
			// In the PASSWORD_WAITING_STATE, green light is off and red light is on.
			green_light_tmp = 1'b0;
			red_light_tmp = 1'b1;
			
			// 7-segment displays are showing EP.
			hex1 = 7'b000_0110;
			hex2 = 7'b000_1100;
		
		end
		
		WRONG_PASSWORD_STATE:
		begin
		
			// In the WRONG_PASSWORD_STATE, green light is off and red light is on.
			green_light_tmp = 1'b0;
			red_light_tmp = 1'b1;
			
			// 7-segment displays are showing W.
			hex1 = 7'b110_0001;
			hex2 = 7'b100_0011;
		
		end
		
		CORRECT_PASSWORD_STATE:
		begin
		
			// In the CORRECT_PASSWORD_STATE, red light is off and green light is on.
			green_light_tmp = 1'b1;
			red_light_tmp = 1'b0;
			
			// 7-segment displays are showing CP.
			hex1 = 7'b100_0110;
			hex2 = 7'b000_1100;
		
		end
		
		WAIT_STATE:
		begin
		
			// In the WAIT_STATE, green light is off and red light is on.
			green_light_tmp = 1'b0;
			red_light_tmp = 1'b1;
			
			// 7-segment displays are showing SP.
			hex1 = 7'b001_0010;
			hex2 = 7'b000_1100;
		
		end
		
		endcase
	
	end
	
	assign green_light = green_light_tmp;
	assign red_light = red_light_tmp;
	
endmodule

