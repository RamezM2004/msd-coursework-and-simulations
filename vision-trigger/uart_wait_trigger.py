"""
uart_wait_trigger.py

Purpose:
    Raspberry Pi-side UART receiver for the myRIO trigger.

System role:
    myRIO reads the IR/distance sensor.
    When the user is close enough, myRIO sends:

        USER_DETECTED\n
    Raspberry Pi receives this message over UART/USB-TTL and starts gesture recognition.

Typical Raspberry Pi serial ports:
    /dev/ttyUSB0   -> USB-to-TTL adapter
    /dev/ttyACM0   -> some USB serial adapters / microcontrollers
    /dev/serial0   -> Raspberry Pi GPIO UART, if enabled

Typical Windows test ports:
    COM3, COM4, COM5, etc.

Install dependency:
    python3 -m pip install pyserial

Standalone test:
    python3 uart_wait_trigger.py
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Optional

import serial
from serial import SerialException


# =========================
# UART CONFIGURATION
# =========================

@dataclass
class UARTConfig:
    """Configuration for the Raspberry Pi UART receiver."""

    port: str = "/dev/ttyUSB0"        # TODO: replace in lab if needed
    baudrate: int = 9600              # Must match myRIO UART baud rate
    timeout_seconds: float = 0.2      # Serial read timeout
    trigger_message: str = "USER_DETECTED"
    cooldown_seconds: float = 3.0     # Ignore repeated triggers for this time


# =========================
# LOW-LEVEL SERIAL HELPERS
# =========================

def open_uart(config: UARTConfig) -> serial.Serial:
    """
    Open UART serial connection.

    Returns:
        serial.Serial object

    Raises:
        SerialException if the port cannot be opened.
    """

    ser = serial.Serial(
        port=config.port,
        baudrate=config.baudrate,
        timeout=config.timeout_seconds,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
    )

    # Give USB serial adapter a moment to settle.
    time.sleep(0.5)
    ser.reset_input_buffer()
    return ser


def read_uart_line(ser: serial.Serial) -> Optional[str]:
    """
    Read one line from UART and decode it safely.

    Returns:
        Clean string without \r/\n, or None if no line was received.
    """

    raw = ser.readline()

    if not raw:
        return None

    try:
        return raw.decode("utf-8", errors="ignore").strip()
    except UnicodeDecodeError:
        return None


# =========================
# MAIN WAIT FUNCTION
# =========================

def wait_for_user_detected(
    port: str = "/dev/ttyUSB0",
    baudrate: int = 9600,
    timeout: Optional[float] = None,
    trigger_message: str = "USER_DETECTED",
    verbose: bool = True,
) -> bool:
    """
    Wait until myRIO sends USER_DETECTED over UART.

    Args:
        port:
            Serial port name. On Raspberry Pi, usually /dev/ttyUSB0.
        baudrate:
            Must match the baud rate configured in LabVIEW/myRIO.
        timeout:
            Maximum waiting time in seconds.
            If None, wait forever.
        trigger_message:
            Expected trigger line from myRIO.
        verbose:
            Print received messages and status.

    Returns:
        True  -> trigger received
        False -> timeout or UART error
    """

    config = UARTConfig(
        port=port,
        baudrate=baudrate,
        trigger_message=trigger_message,
    )

    start_time = time.time()

    try:
        ser = open_uart(config)
    except SerialException as exc:
        print(f"UART ERROR: Could not open serial port {port}: {exc}")
        return False

    if verbose:
        print("UART receiver started.")
        print(f"Port: {port}")
        print(f"Baudrate: {baudrate}")
        print(f"Waiting for: {trigger_message}")
        print("Press Ctrl+C to stop.\n")

    try:
        with ser:
            while True:
                if timeout is not None and (time.time() - start_time) >= timeout:
                    if verbose:
                        print("UART wait timed out.")
                    return False

                line = read_uart_line(ser)

                if line is None:
                    continue

                if verbose:
                    print(f"Received: {line}")

                if line == trigger_message:
                    if verbose:
                        print("Trigger accepted: USER_DETECTED")
                    return True

    except KeyboardInterrupt:
        if verbose:
            print("UART receiver stopped by user.")
        return False

    except SerialException as exc:
        print(f"UART ERROR while reading: {exc}")
        return False


# =========================
# CONTINUOUS LISTENER
# =========================

def listen_for_triggers(
    port: str = "/dev/ttyUSB0",
    baudrate: int = 9600,
    trigger_message: str = "USER_DETECTED",
    cooldown_seconds: float = 3.0,
) -> None:
    """
    Continuous UART test mode.

    This is useful before integration.
    It keeps listening and prints every accepted USER_DETECTED trigger.
    A cooldown prevents repeated triggers from myRIO from spamming the output.
    """

    config = UARTConfig(
        port=port,
        baudrate=baudrate,
        trigger_message=trigger_message,
        cooldown_seconds=cooldown_seconds,
    )

    try:
        ser = open_uart(config)
    except SerialException as exc:
        print(f"UART ERROR: Could not open serial port {port}: {exc}")
        return

    print("Continuous UART listener started.")
    print(f"Port: {port}")
    print(f"Baudrate: {baudrate}")
    print(f"Expected trigger: {trigger_message}")
    print(f"Cooldown: {cooldown_seconds} seconds")
    print("Press Ctrl+C to stop.\n")

    last_trigger_time = 0.0

    try:
        with ser:
            while True:
                line = read_uart_line(ser)

                if line is None:
                    continue

                print(f"Received: {line}")

                current_time = time.time()

                if line == trigger_message:
                    if current_time - last_trigger_time >= cooldown_seconds:
                        last_trigger_time = current_time
                        print("✅ Valid trigger received. Start gesture recognition here.\n")
                    else:
                        print("Ignored repeated trigger during cooldown.\n")

    except KeyboardInterrupt:
        print("Continuous UART listener stopped.")

    except SerialException as exc:
        print(f"UART ERROR while reading: {exc}")


# =========================
# STANDALONE TEST
# =========================

if __name__ == "__main__":
    # Change this in the lab if your adapter appears as another port.
    # Raspberry Pi common value: "/dev/ttyUSB0"
    # Windows test example: "COM3"
    SERIAL_PORT = "/dev/ttyUSB0"
    BAUDRATE = 9600

    listen_for_triggers(
        port=SERIAL_PORT,
        baudrate=BAUDRATE,
        trigger_message="USER_DETECTED",
        cooldown_seconds=3.0,
    )
