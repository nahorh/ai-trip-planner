from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""
        @tool
        def estimate_total_hotel_cost(price_per_night:str, total_days:float) -> float:
            """Calculate total hotel cost"""
            return self.calculator.multiply(price_per_night, total_days)
        
        @tool
        def calculate_total_expense(costs: list[float] | float, extra_costs: list[float] | None = None) -> float:
            """Calculate total expense of the trip"""
            if isinstance(costs, list):
                values = [float(c) for c in costs]
            else:
                values = [float(costs)]
            if extra_costs:
                values.extend(float(c) for c in extra_costs if c is not None)
            return self.calculator.calculate_total(*values)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]