from scr.basic_math_utilities import BasicMathUtilities
import logging
import pytest

logger = logging.getLogger('pytest_logger')


@pytest.fixture(autouse=True)
def session_thing():
    logger.info('<{}> log setup'.format(__name__))
    yield
    logger.info('<{}> log teardown'.format(__name__))


@pytest.fixture(scope="session")
def value_01():
   yield 100


@pytest.fixture(scope="session")
def value_02():
   yield 0


def test_add(value_01, value_02):
    assert BasicMathUtilities.add(value_01, value_02) == 100
    
    
def test_divide_zero(value_01, value_02):
    assert BasicMathUtilities.divide(value_01, value_02)
 
    
    
    # assert BasicMathUtilities.divide(value_01, value_02) 
    
    
   
    # with pytest.raises(ZeroDivisionError) as excinfo:  
        # BasicMathUtilities.divide(value_01, value_02) 

    
    
    # assert BasicMathUtilities.divide(value_01, value_02) == 20


    #with pytest.raises(ZeroDivisionError) as excinfo:  
        #BasicMathUtilities.divide(value_01, value_02)
    #assert str(excinfo.value) == "Division by zero is not allowed"  
