"""Investor module"""
import ast
import json
import random


class Investor:
    '''Class investor
    Attributes:
        data (type:dict) - dictionary with all data
    Methods:
        static extract_locations()
        static extract_specialties()
        static extract_operational_models()
        process_data()
        display_info()
        predict_rating_growth()
        is_competitor()
        find_potential_partners()



    '''
    def __init__(self, data: dict):
        '''The initializer'''
        self.full_name = data.get("name", "Unknown")
        self.locations = None
        self.__sector = None
        self.rating = None
        self.category = None
        self.specialties = None
        self.operational_models = None

        self.process_data(data)

    def __str__(self):
        return (
            f"Investor Name: {self.full_name}\n"
            f"Locations: {self.locations}\n"
            f"Sector: {self.__sector}\n"
            f"Rating: {self.rating}\n"
            f"Category: {self.category}\n"
            f"Specialties: {self.specialties}\n"
            f"Operational Models: {self.operational_models}"
        )
    @staticmethod
    def extract_locations(place_data: list[dict]) -> list:
        '''Extracts locations'''
        results = []
        for place in place_data:
            city_name = place.get("city", {}).get("name", "")
            state_name = place.get("state", {}).get("name", "")
            results.append(f"{city_name}, {state_name}")
        return results

    @staticmethod
    def extract_specialties(specialty_info: list[dict[str, str]]) -> set:
        '''Extracts professions'''
        results = set()
        for field in specialty_info:
            results.add(field.get("name", ""))
        return results

    @staticmethod
    def extract_operational_models(model_data: dict) -> set:
        '''Ectrsct oper modules'''
        paths = model_data.get("fullPathList", [{}])
        results = set()
        for item in paths:
            results.add(item.get("name", ""))
        return results

    def process_data(self, data: dict):
        '''Processes the data'''
        self.locations = self.extract_locations(data.get("locations", []))
        self.rating = data.get("tracxnInvestmentScore", 0)
        self.sector = data.get("domain", "")
        self.category = data.get("investorType", "")
        self.specialties = self.extract_specialties(data.get("practiceAreaList", []))
        self.operational_models = self.extract_operational_models(data.get("businessModelList", [{}])[0])

    def display_info(self) -> str:
        return f"Investor: {self.full_name} | Locations: {', '.join(self.locations)} | Sector: {self.sector} | Rating: {self.rating}"

    @property
    def sector(self) -> str:
        '''sector property'''
        if not self.__sector:
            return "Sector not specified"
        return self.__sector

    @sector.setter
    def sector(self, new_sector: str):
        '''sector setter'''
        self.__sector = new_sector

    def predict_rating_growth(self, years: int) -> float:
        """
        Predicts the rating growth
        """
        projected_rating = self.rating
        for _ in range(years):
            annual_growth = random.uniform(0, 0.1)
            projected_rating *= (1 + annual_growth)
        return projected_rating

    def is_competitor(self, other: 'Investor') -> bool:
        """
        checks whether investors are competitors
        """
        return (self.category == other.category and
                self.specialties.intersection(other.specialties) and
                self.operational_models.intersection(other.operational_models))

    def find_potential_partners(self, partners: list['Investor']) -> list['Investor']:
        """
        finds potential partners
        """
        return [partner for partner in partners if self.is_competitor(partner)]


sample_data_1 = {
    "name": "John Doe Ventures",
    "locations": [{"city": {"name": "New York"}, "state": {"name": "NY"}}],
    "tracxnInvestmentScore": 85,
    "domain": "Technology",
    "investorType": "Venture Capital",
    "practiceAreaList": [{"name": "FinTech"}, {"name": "AI"}],
    "businessModelList": [{"fullPathList": [{"name": "B2B"}, {"name": "SaaS"}]}]
}

sample_data_2 = {
    "name": "Jane Smith Investments",
    "locations": [{"city": {"name": "San Francisco"}, "state": {"name": "CA"}}],
    "tracxnInvestmentScore": 78,
    "domain": "Healthcare",
    "investorType": "Venture Capital",
    "practiceAreaList": [{"name": "MedTech"}, {"name": "AI"}],
    "businessModelList": [{"fullPathList": [{"name": "B2C"}, {"name": "SaaS"}]}]
}


investor1 = Investor(sample_data_1)
investor2 = Investor(sample_data_2)



