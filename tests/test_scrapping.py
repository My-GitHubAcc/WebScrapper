from utils.scrapper import Scrapper

class TestScrapping:
    url = "http://contrastlens.com/boutique/"
    def test_page_can_be_fetched(_):
        
        scrapper = Scrapper(TestScrapping.url)
        response = scrapper._getPage(TestScrapping.url)

        assert response is not None

    def test_page_contents_can_parsed(_):
        scrapper = Scrapper(TestScrapping.url)
        assert scrapper.soup is not None

    def test_can_get_element_by_id(_):
        scrapper = Scrapper(TestScrapping.url)
        elements = scrapper.getElementsByClass('fusion-top-frame')
        assert elements is not None

    def test_can_fetch_proper_data(_):
        scrapper = Scrapper(TestScrapping.url)
        element = scrapper.getElementsByClass('woof_term_4655')
        #label = element[0].text
        assert len(element) > 0
    
    def test_can_fetch_elements_by_attribute_values(_):
        scrapper = Scrapper(TestScrapping.url)
        elements = scrapper.getElementsBySelectors({'data-tax': "pa_lens-material"})

        assert len(elements) > 0