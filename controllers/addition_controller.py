"""
Module for addition controller.

This module provides functions to perform addition on lists of numbers
and handle addition requests using Python's multiprocessing pool.
"""
import logging
from multiprocessing import Pool
import datetime
from models.addition_models import AdditionRequest, AdditionResponse


# Setup logging
from config import LOG_FORMAT, LOG_LEVEL
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def add_numbers(numbers):
    """
    Function to perform addition on a list of numbers.

    Args:
        numbers (list): List of numbers to be added.

    Returns:
        int: The sum of the numbers.
    """
    try:
        result = sum(numbers)
        return result
    except TypeError as err:
        logger.error("Error occurred while adding numbers: %s", err)
        return None


def perform_addition(request: AdditionRequest):
    """
    Function to perform addition on input lists of integers using Python's
    multiprocessing pool.

    Args:
        request (AdditionRequest): The request object containing batchid and
        payload.

    Returns:
        AdditionResponse: The response object containing batchid, response,
        status, started_at, and completed_at.
    """
    batchid = request.batchid
    payload = request.payload

    logger.info("Starting addition process for batch %s...", batchid)
    started_at = datetime.datetime.now().isoformat()

    try:
        with Pool() as pool:
            results = pool.map(add_numbers, payload)
    except Exception as err:
        logger.error("Error occurred while performing additionfor batch %s: %s", batchid, err)
        return None

    completed_at = datetime.datetime.now().isoformat()

    response = AdditionResponse(
        batchid=batchid,
        response=results,
        status="complete",
        started_at=started_at,
        completed_at=completed_at
    )

    logger.info("Addition process completed for batch %s.", batchid)

    return response
