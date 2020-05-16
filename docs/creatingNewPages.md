[back to readme](../../../)

# Creating New Pages

Several pages are included in `Empiric!` by default.  Further pages can be added, thereby being tailored to the experiment you have in mind.  To make the implementation as simple as possible, several simple steps are described in the following.

1. Generate a template by executing the following command:
```python
from Empiric import Experiment
experiment = Experiment()
experiment.createPageStructure()
```
The following files are accordingly added to your path:
* `pages/_PageExample.py` – This is the code of your page you will implement.
* `templates/_PageExample.html` – This is the template of your page you will implement.
* `package.json` – Contains a list of all JavaScript libraries that you need for your page
* `pages/__init__.py` and `.yarnrc` – Two files needed behind the scenes; they are not of interest for you
2. Rename the files to `pages/Page???.py` and `templates/page???.html`, where `???` is some string that serves as a key to recognize the page.
3. Rename all occurances of `pageExample` and `PageExample` in the this file accordingly, while paying attention to capitalization.
4. In the file where your manuscript is defined, add the following import:
```python
from pages.Page??? import page???
```
5. Now, you can use your new page in the manuscript by adding
```python
page???(m)
```
6. Congrats, you made it!  Your first page works.
7. You can start tailoring the page to your needs.  To do so, modify the Python and the HTML file accordingly.
8. If your page needs some JavaScript library that has not yet been loaded automatically, you have to add this to the `package.json`, which you find in your working directy.  Therafter, install the JavaScript library using Yarn in your working directy:
```bash
yarn install
```
Then, you can load the library accordingly by inserting corresponding statements in the header block of the file `templates/page???.html`:
```html
{% block pageHeader %}
  <link rel="stylesheet" href="{{url_for('static', filename='libs/path/to/file.css')}}"/>
  <script src="{{url_for('static', filename='libs/path/to/file.js')}}"></script>
{% endblock %}
``` 
