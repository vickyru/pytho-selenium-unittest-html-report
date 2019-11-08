# pytho-selenium-unittest-html-report

This repo is consisting of the basic structure of a POM based test automation framework. Followings are the tech-spec of framework
- Python
- Selenium
- Unittest
- HTML Test Runner Reports
## Assumption
- Python installed 
- Module belowa are installed
    - html-testRunner   1.2.1
    - pip               19.3.1
    - selenium          3.141.0
    - webdriver-manager 2.2.0
    ```
    pip install -U <module-name-here>
    ```
# How to use framework
## Clone repo
```
git clone https://github.com/vickyru/pytho-selenium-unittest-html-report.git 
```
## Run framework
### Open terminal and run below command from project workspace
```
python -m test.specs.calculator_test
```
# Reports
Once framework run successfully it will generate the report under folder name html-report