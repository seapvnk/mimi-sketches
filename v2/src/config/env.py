def load_env(file_path: str) -> dict:
    """
    Read env file
    """
    env_vars = {}

    with open(file_path, 'r') as env_file:
        for line in env_file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                env_vars[key] = value

    return env_vars

env = load_env('.env')