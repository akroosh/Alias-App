# Alias App
App for creating aliases for objects.

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3</li>
  <li>pip3 to install dependencies</li>
  <li>SQLite</li>
  </ul>

<h3>Installing packages</h3>
<h4>Mac OS:</h4>
<ol>
 <li>Run <code>virtualenv env</code> to create virtual environment </li>
 <li>Activate it by <code>source env/bin/activate</code></li>
 <li>Run <code>pip3 install -r requirements.txt</code></li>
 </ol>


<h3>Setting up the local DB</h3>
<ol>
<li>Cd into the app directory</li>
<li>Run <code>python3 manage.py makemigrations</code></li>
<li><code>python3 manage.py migrate</code></li>
</ol>

<h3>Running the tests</h3>
<p>Run using <code>python3 manage.py test alias.tests</code></p>