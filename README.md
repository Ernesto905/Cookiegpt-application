# COOKIEGPT - A simple application, overengineered 👩‍🔧🔧⚙️🚀

## Quick Setup, without the pipeline

### Ensure you are in the src file and that you have python >= 3.7 installed 

1. Create a new virtual environment:

   ```bash/zsh
   $ python -m venv venv
   $ . venv/bin/activate
   ```

2. Install the requirements:

   ```bash/zsh
   $ pip install -r requirements.txt
   ```

3. Make a copy of the example environment variables file:

   ```bash/zsh
   $ cp .env.example .env
   ```

4. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

5. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!

## Booting up the redis database
6. Ensure you have redis installed in your local machine

7. run the following command to boot up a redis server $ redis-server

### Note: There is a running counter in the redis db. To reset this, run $ redis-cli set count 0