from os.path import abspath, dirname, join

HERE = dirname(abspath(__file__))

ODT_TEMPLATE_PATH = join(HERE, 'template.odt')
CONTENT_SCREENSHOT_PATH = join(HERE, 'content_screenshot.txt')
RENDERED_CONTENT_SCREENSHOT = join(HERE, 'rendered_content_screenshot.txt')
