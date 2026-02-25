import pytest
from unittest.mock import Mock, patch
from app.calculation import Calculation
from app.history import LoggingObserver, AutoSaveObserver
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig

# Sample setup for mock calculation
calculation_mock = Mock(spec=Calculation)
calculation_mock.operation = "addition"
calculation_mock.operand1 = 5
calculation_mock.operand2 = 3
calculation_mock.result = 8

# Test cases for LoggingObserver

@patch('logging.info')
def test_logging_observer_logs_calculation(logging_info_mock):
    observer = LoggingObserver()
    observer.update(calculation_mock)
    logging_info_mock.assert_called_once_with(
        "Calculation performed: addition (5, 3) = 8"
    )

def test_logging_observer_no_calculation():
    observer = LoggingObserver()
    with pytest.raises(AttributeError):
        observer.update(None)  # Passing None should raise an exception as there's no calculation

# Test cases for AutoSaveObserver

def test_autosave_observer_triggers_save():
    calculator_mock = Mock(spec=Calculator)
    calculator_mock.config = Mock(spec=CalculatorConfig)
    calculator_mock.config.auto_save = True
    observer = AutoSaveObserver(calculator_mock)
    
    observer.update(calculation_mock)
    calculator_mock.save_history.assert_called_once()

@patch('logging.info')
def test_autosave_observer_logs_autosave(logging_info_mock):
    calculator_mock = Mock(spec=Calculator)
    calculator_mock.config = Mock(spec=CalculatorConfig)
    calculator_mock.config.auto_save = True
    observer = AutoSaveObserver(calculator_mock)
    
    observer.update(calculation_mock)
    logging_info_mock.assert_called_once_with("History auto-saved")

def test_autosave_observer_does_not_trigger_save_when_disabled():
    calculator_mock = Mock(spec=Calculator)
    calculator_mock.config = Mock(spec=CalculatorConfig)
    calculator_mock.config.auto_save = False
    observer = AutoSaveObserver(calculator_mock)
    
    observer.update(calculation_mock)
    calculator_mock.save_history.assert_not_called()

# Additional negative test cases for AutoSaveObserver

def test_autosave_observer_invalid_calculator():
    with pytest.raises(TypeError):
        AutoSaveObserver(None)  # Passing None should raise a TypeError

def test_autosave_observer_no_calculation():
    calculator_mock = Mock(spec=Calculator)
    calculator_mock.config = Mock(spec=CalculatorConfig)
    calculator_mock.config.auto_save = True
    observer = AutoSaveObserver(calculator_mock)
    
    with pytest.raises(AttributeError):
        observer.update(None)  # Passing None should raise an exception


def test_logging_observer_init():
    """Test LoggingObserver can be instantiated."""
    observer = LoggingObserver()
    assert observer is not None


# ── CalculatorMemento tests ──
from app.calculator_memento import CalculatorMemento
from decimal import Decimal

def test_memento_to_dict():
    calc = Calculation(operation="Addition", operand1=Decimal("2"), operand2=Decimal("3"))
    memento = CalculatorMemento(history=[calc])
    result = memento.to_dict()
    assert 'history' in result
    assert 'timestamp' in result
    assert len(result['history']) == 1
    assert result['history'][0]['operation'] == 'Addition'


def test_memento_from_dict():
    calc = Calculation(operation="Addition", operand1=Decimal("2"), operand2=Decimal("3"))
    memento = CalculatorMemento(history=[calc])
    data = memento.to_dict()
    restored = CalculatorMemento.from_dict(data)
    assert len(restored.history) == 1
    assert restored.history[0].operation == "Addition"
    assert restored.history[0].operand1 == Decimal("2")
    assert restored.history[0].result == Decimal("5")