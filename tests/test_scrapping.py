from utils.scrapper import Scrapper

class TestScrapping:
    url = "http://contrastlens.com/boutique/"
    def test_page_can_be_fetched(_):
        
        scrapper = Scrapper()
        response = scrapper.getPage(TestScrapping.url)

        assert response is not None

    def test_page_contents_can_parsed(_):
        scrapper = Scrapper()
        scrapper.getContent(TestScrapping.url)
        assert scrapper.soup is not None

    def test_can_get_element_by_id(_):
        scrapper = Scrapper()
        scrapper.getContent(TestScrapping.url)
        elements = scrapper.getElementsByClass('fusion-top-frame')
        assert elements is not None

    def test_can_fetch_proper_data(_):
        scrapper = Scrapper()
        scrapper.getContent(TestScrapping.url)
        element = scrapper.getElementsByClass('woof_term_4655')
        #label = element[0].text
        assert len(element) > 0
    
    def test_can_fetch_elements_by_attribute_values(_):
        scrapper = Scrapper()
        scrapper.getContent(TestScrapping.url)
        elements = scrapper.getElementsBySelectors({'data-tax': "pa_lens-material"})

        assert len(elements) > 0