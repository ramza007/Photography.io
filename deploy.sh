#!/bin/bash

# Step 1: Collect static files
#echo "Collecting static files..."
#heroku run python3 manage.py collectstatic

# Step 2: Push changes to GitHub
echo "Pushing changes to GitHub Master Branch..."
git push origin master

# Step 3: Push to Heroku
echo "Pushing to Heroku..."
git push heroku master

# Step 4: Run migrations on Heroku
#echo "Running migrations on Heroku..."
#heroku run python manage.py migrate

echo "Returning you back to DEV"
git checkout dev
