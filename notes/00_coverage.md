# Notes on `coverage` Module

## Commands

* `coverage run` - Run a Python program and measure code coverage
* `coverage report` - Report coverage stats
* `coverage html` - Generate an HTML report
* `coverage run .\manage.py test things -v 2` - Run tests and measure code coverage
* `coverage run --omit='**/migrations/*' .\manage.py test things -v 2`
* `coverage report -m` - Report coverage stats with missing lines
