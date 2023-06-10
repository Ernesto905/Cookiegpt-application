# COOKIEGPT - A simple application, overengineered

## Quick Setup, without the pipeline

### Ensure you are in the src file and that you have python 3.9.6 installed  

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