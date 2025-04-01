'''Module for testing comics module'''
import unittest
from comics import Element, Panel, Comics, Image, Text, FixedElementError, PositionNotEmptyError

class TestComics(unittest.TestCase):
    '''Tests the comics class'''
    def test_text_simple(self):
        '''Simple test case that tests Text class'''
        text_test = Text("A cat squeezes into a tiny box", "Perfect fit. No doubts here.")
        self.assertEqual(text_test.name, "A cat squeezes into a tiny box")
        self.assertEqual(text_test.text, 'Perfect fit. No doubts here.')
    def test_image_simple(self):
        '''Simple test case that tests Image class'''
        test_image = Image('A cat squeezes into a tiny box', "image1.png")
        self.assertEqual(test_image.name, 'A cat squeezes into a tiny box')
        self.assertEqual(test_image.path, "image1.png")
        self.assertEqual(test_image.is_fixed, False)
        self.assertEqual(test_image.position, None)
    def test_panem_simple(self):
        '''Tests Panel class'''
        self.assertEqual(Panel('A cat squeezes into a tiny box').title, 'A cat squeezes into a tiny box')
    def test_comics_simple(self):
        '''Simple test case that tests Comics class'''
        story = Comics('Sofiyka', 'The best moments with my lovely-cutie-pootie cat')
        self.assertEqual(story.author, 'Sofiyka') 
        self.assertEqual(story.title, 'The best moments with my lovely-cutie-pootie cat')
        self.assertEqual(story.panels, [])
        self.assertEqual(str(story), "This comics is empty.")
    def test_add_image_to_panel(self):
        '''Tests is ewverythin's fine if you try to add image to panel'''
        panel = Panel('Test Panel')
        image = Image('Test Image', 'test.png')
        panel.add_element(image, 'middle')
        self.assertEqual(panel.elements['middle'], image)
        self.assertEqual(image.position, (panel, 'middle'))

    def test_position_not_empty_error(self):
        """Tests that adding an element to an occupied position raises an error."""
        panel = Panel('Test Panel')
        panel.add_element(Text('Text1', 'First text'), 'top')
        with self.assertRaises(PositionNotEmptyError):
            panel.add_element(Text('Text2', 'Second text'), 'top')


if __name__ == '__main__':
    unittest.main()
