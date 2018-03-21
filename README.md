1. Install Redis:

    ```
    sudo apt-get install redis-server
    ```

2. Init virtual-environment:

    ```
    virtualenv venv
    ```

3. Install requirements:

    ```
    . venv/bin/activate && pip install -r requirements.txt
    ```

3. Apply db migrations:
    ```
    . venv/bin/activate && python manage.py migrate
    ```

4. Spawn celery worker

   ```
   . venv/bin/activate && celery -A coralogix_test worker -l info
   ```

5. Spawn celery beat

   ```
   . venv/bin/activate && celery -A coralogix_test beat -l info
   ```

6. Run Django:

   ```
   . venv/bin/activate && python manage.py runserver
   ```
