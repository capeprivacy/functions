import pendulum

def cape_handler(timezone_bytes):
    # Convert timezone as bytes to string
    timezone = timezone_bytes.decode()
    # Get current time based on timezone
    now = pendulum.now(timezone)
    return now.to_time_string()