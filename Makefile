pwa:
	python3 -m playwright codegen https://admin-tg-test.chunsutech.com/
pwc:
	python3 -m playwright codegen https://client-tg-test.chunsutech.com/


t:
	python3 -m pytest -s -v TestCase --tracing=retain-on-failure --screenshot=only-on-failure --maxfail=1
dt:
	PWDEBUG=1 python3 -m pytest -s -v cases/test_product.py
tree:
	tree -I node_modules > tree.text
req:
	pip3 freeze > requirements.txt
