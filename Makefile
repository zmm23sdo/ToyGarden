pw:
	python3 -m playwright codegen https://admin-tg-dev.chunsutech.com/

t:
	python3 -m pytest -s -v TestCase --tracing=retain-on-failure --screenshot=only-on-failure --maxfail=1
dt:
	PWDEBUG=1 python3 -m pytest -s -v TestCase
tree:
	tree -I node_modules > tree.text
req:
	pip3 freeze > requirements.txt
