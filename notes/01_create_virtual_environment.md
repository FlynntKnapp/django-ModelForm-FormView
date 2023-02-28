# Process

1. Start in project root directory:

    * Definition of 'project root':
      * THE_DEFINITION_OF_PROJECT_ROOT
    * `pwd`:

      ```powershell
      PS C:\Users\FlynntKnapp\Programming\examples\django\forms_basic_model_form> pwd     

      Path
      ----
      C:\Users\FlynntKnapp\Programming\examples\django\forms_basic_model_form

      PS C:\Users\FlynntKnapp\Programming\examples\django\forms_basic_model_form>
      ```

1. Create `pipenv` virtual environment and install `django` and `docutils`:

    * `pipenv install django==4.1.7 docutils==0.19`

1. Create basic Django project/site/config:

    * `django-admin startproject config .`

1. Test development server:
  
      * `python manage.py runserver`

1. Verify Django green rocket at server root:

    * <http://localhost:8000/>

1. Stop development server:

    * <kbd>Ctrl</kbd> + <kbd>C</kbd>

1. Add `.gitignore` file to repository:

    * <https://www.toptal.com/developers/gitignore/>
      * <https://www.toptal.com/developers/gitignore/api/python,django>
    * `.vscode` directory is excluded from `.gitignore` so we can use it to set up VS Code for running Django and running Django Tests.

1. Add `things` application:

    * `django-admin startapp things`

1. Add `Thing` model to [`things/models.py`](../things/models.py):

    ```python
    from django.db import models

    class Thing(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name
    ```
