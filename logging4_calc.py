import logging

# Get the root logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set logger level to DEBUG to process all levels

# Define the log message format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create a FileHandler to write logs to 'sample.log'
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.DEBUG)  # Set handler level to DEBUG to capture all levels
file_handler.setFormatter(formatter)

# Create a StreamHandler to print logs to console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Set handler level to INFO for console output
stream_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Define functions for logging demonstration
def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

# Example usage of logging
if __name__ == '__main__':
    logger.info("Starting calculations...")

    # Perform addition and log the result
    result_add = add(10, 5)
    logger.debug(f"Addition result: {result_add}")

    # Perform subtraction and log the result
    result_subtract = subtract(20, 7)
    logger.debug(f"Subtraction result: {result_subtract}")

    # Perform multiplication and log the result
    result_multiply = multiply(8, 4)
    logger.debug(f"Multiplication result: {result_multiply}")

    # Try a division operation that may raise an exception, and log any error
    try:
        result_divide = divide(15, 0)
    except ValueError as e:
        logger.error(f"Error occurred during division: {e}")

    logger.info("Calculations completed.")
