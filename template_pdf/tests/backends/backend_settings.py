from os.path import abspath, dirname, join

HERE = dirname(abspath(__file__))

ODT_TEMPLATE_PATH = join(HERE, 'template.odt')
CONTENT_SCREENSHOT_PATH = join(HERE, 'content_screenshot.txt')
RENDERED_CONTENT_SCREENSHOT = join(HERE, 'rendered_content_screenshot.txt')

HTML_TEMPLATE_PATH = join(HERE, 'template.html')
RENDERED_CONTENT_HTML_TEMPLATE_SCREENSHOT = join(HERE,
                                                 'rendered_content_html_template_screenshot.txt')
