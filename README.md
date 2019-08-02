# xss-example

First, I converted the assignment to a template view instead of just embedded html

Then I sterilized the input from the user, using html.escape and stripping '
before saving to the database.

This way the raw scripts are saved into the data in a clean form instead of being
sterilized just before rendering.