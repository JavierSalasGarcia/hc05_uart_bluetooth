if “1” in rxData:
	uart1.write(“Encendiendo\r\n”)
	print(“LED on\r\n”)
	led.value(1)
elif “0” in rxData:
uart1.write(“Apagando\r\n”)
	print(“LED off\r\n”)
	led.value(0)
elif “A” in rxData:
uart1.write(“led y buzzer: ON\r\n”)
	print(“LED, Buzz: on\r\n”)
	led.value(1)
	pwm0.freq(1000)
	pwm0.duty_u16(32000)
elif “B” in rxData:
uart1.write(“led y buzzer: OFF\r\n”)
	print(“LED, Buzz: off\r\n”)
	led.value(0)
	pwm0.deinit()
elif “C” in rxData:
uart1.write(“Escrito por Javier Salas G\r\n”)
	print(“UART y Bluetooth\r\n”)
