import yaml
from module import Site
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata['address'])

def test():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element('xpath', x_selector1)
    input1.clear()
    input1.send_keys(testdata['username'])
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element('xpath', x_selector2)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn_selector = 'button'
    btn = site.find_element('css', btn_selector)
    btn.click()
    add_btn_selector = """//*[@id="create-btn"]"""
    add_btn = site.find_element('xpath', add_btn_selector)
    add_btn.click()
    x_selector3 = '//*[@id="create-item"]/div/div/div[1]/div/label/input'
    input3 = site.find_element('xpath', x_selector3)
    input3.send_keys(testdata['title'])
    save_btn_selector = """// *[ @ id = "create-item"] / div / div / div[7] / div / button / span"""
    save_btn = site.find_element('xpath', save_btn_selector)
    save_btn.click()
    time.sleep(testdata['sleep_time'])
    x_selector4 = """//*[@id="app"]/main/div/div[1]/h1"""
    title_label2 = site.find_element('xpath', x_selector4)
    text = title_label2.text
    assert text == f'{testdata["title"]}'
