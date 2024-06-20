import os

# username = os.environ.get('BROWSERSTACK_USERNAME')
# accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY')
buildName = os.environ.get('BROWSERSTACK_BUILD_NAME')
# local = os.environ.get('BROWSERSTACK_LOCAL')
# localIdentifier = os.environ.get('BROWSERSTACK_LOCAL_IDENTIFIER')

capabilities = {
    'platformName': 'mac',
    'browserName': 'safari',
    'browserVersion': 'latest',
    'build': os.environ.get('BROWSERSTACK_BUILD_NAME'),  # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
    'projectName': 'Testing using Mac - Safari',
    'debug': 'true',
    'networkLogs': 'true'
}
