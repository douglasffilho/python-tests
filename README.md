# python-tests
A Python Test App using Flask

### Setup
- Create Virtualenv:
    ```bash
    sh bin/create_venv.sh
    ```

- Configure python from local virtualenv on interpreter settings
  ![PyCharmVenvSetting](https://user-images.githubusercontent.com/23297944/84283510-742b2600-ab11-11ea-83b4-0b654182a619.png)

### Run Application
```bash
PYTHONUNBUFFERED=1 PYTHONPATH=src ./venv/bin/python ./bin/run_application.py
```
