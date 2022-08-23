import pendulum


def cape_handler(timezone_bytes):
    timezone = timezone_bytes.decode()
    now = pendulum.now(timezone)
    return now.to_time_string()
