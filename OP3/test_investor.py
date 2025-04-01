'''Test investor module'''
import unittest
import random
from investor import Investor

class TestInvestor(unittest.TestCase):
    '''The class that tests Investor class
    Methods:
        setUp()- sets up the instances
        test_init() - tests init
        test_sector_property()
        test_predict_rating_grow()
        test_is_competitor()
        test_finding_partners()

    '''
    def setUp(self):
        self.investor_data = {
            "name": "Sophia Mandryk",
            "locations": [{"city": {"name": "New York"}, "state": {"name": "NY"}}],
            "tracxnInvestmentScore": 50,
            "domain": "Technology",
            "investorType": "Venture Capitalist",
            "practiceAreaList": [{"name": "AI"}, {"name": "Fintech"}],
            "businessModelList": [{"fullPathList": [{"name": "B2B"}, {"name": "SaaS"}]}]
        }
        self.investor = Investor(self.investor_data)
    
    def test_init(self):
        '''Testing init'''
        self.assertEqual(self.investor.full_name, "Sophia Mandryk")
        self.assertEqual(self.investor.locations, ["New York, NY"])
        self.assertEqual(self.investor.rating, 50)
        self.assertEqual(self.investor.sector, "Technology")
        self.assertEqual(self.investor.category, "Venture Capitalist")
        self.assertEqual(self.investor.specialties, {"AI", "Fintech"})
        self.assertEqual(self.investor.operational_models, {"B2B", "SaaS"})
    
    def test_display(self):
        '''Testing display'''
        expected_info = "Investor: Sophia Mandryk | Locations: New York, NY | Sector: Technology | Rating: 50"
        self.assertEqual(self.investor.display_info(), expected_info)
    
    def test_sector_property(self):
        '''Testing sector property'''
        self.investor.sector = "Healthcare"
        self.assertEqual(self.investor.sector, "Healthcare")
    
    def test_predict_rating_grow(self):
        '''testing rating grow'''
        random.seed(1)
        projected_rating = self.investor.predict_rating_growth(5)
        self.assertGreater(projected_rating, 50)
    
    def test_is_competitor(self):
        '''Testing on competitor info'''
        competitor_data = self.investor_data.copy()
        competitor = Investor(competitor_data)
        self.assertTrue(self.investor.is_competitor(competitor))
    
    def test_finding_partners(self):
        '''Testing finding partners'''
        partner_data = self.investor_data.copy()
        partner = Investor(partner_data)
        non_partner_data = partner_data.copy()
        non_partner_data["investorType"] = "Angel Investor"
        non_partner = Investor(non_partner_data)
        
        partners = self.investor.find_potential_partners([partner, non_partner])
        self.assertIn(partner, partners)
        self.assertNotIn(non_partner, partners)

if __name__ == "__main__":
    unittest.main()
