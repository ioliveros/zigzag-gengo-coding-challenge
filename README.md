# zigzag-gengo-coding-challenge

#### you need atleast `python>=3.6`, clone repo via `git`

```sh
~$: git clone https://github.com/ioliveros/zigzag-gengo-coding-challenge
```

#### then navivate to your folder
```sh
~$: cd zizag-gengo-coding-challenge/
```

#### to install on your environment
```sh
~$: python setup.py develop
```

#### if you want to install globally 
```sh
~$: python setup.py install
```

#### to check if package is properly installed
```sh
~$: python -c "import gengo"
```

#### run test
```sh
~$: pytest
```

#### or just run specific test
```sh
~$: pytest tests/test_palindrome.py
```

#### basic usage
```python
>>> import gengo
>>> gengo.is_palindrome('abcdcba')
>>> True
```
