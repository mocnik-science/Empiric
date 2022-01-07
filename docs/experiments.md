[back to readme](../../../)

# Experiments

Experiments are the heart of `Empiric!`  The way the class `Experiment` has been implemented makes possible to run a manuscript – that is, an outline of the pages (experiments, questionnaires, etc.) to show – with only some lines of code:
```python
from Empiric import Experiment

def manuscript(m):
  ...

experiment = Experiment()
experiment.run(manuscript)
```

The command `run` starts the web server and handles everything that is needed to do so in the background.  In particular, it cares about creating the paths necessary to provide static files (such as maps), installing all JavaScript libraries needed, serving the website, organizing the access to the experiments, storing the logs and results, and finally analysing these statistically.  To quit the experiment, just press `CTRL + C`.

Besides including the manuscript as a mandatory argument to `run`, further keyword arguments can be provided.  The following arguments can be used:

| Option | Type | Default | Description |
| ------ | ---- | ------- | ----------- |
| `port` | `Integer` | `8080` | Port that is used to serve the website. |
| `urlRoot` | `String` | '/' | Url root in case a reverse proxy is used.  (This option is despite the fact that the reverse proxy needs to remove the url root from the forwarded requests.) |
| `debug` | `Boolean` | `False` | If run in debug mode, the experiment will automatically restart when the manuscript is modified and saved.  This is useful when writing and modifying the manuscript but should not be used during the actual experiment. |
| `openBrowser` | `Boolean` | `True` | Defines whether the website should be opened automatically in a browser after starting the experiment. |
| `pathStatic` | `String` | `static` | Path where the static files (JavaScript libraries, images, and maps) are stored. |
| `pathTemplates` | `String` | `templates` | Path where the templates for user-defined pages are stored. |
| `mode` | `MODE` | `MODE.LOCAL` | Mode in which to run the experiment.  For further information, see Section [Modes](#modes). |
| `numberOfAccessCodes` | `Integer` | `1000` | Number of the access codes to generate when starting the server.  For further information, see Section [Modes](#modes). |
| `statisticsPassword` | `String` | `None` | Password to be used for the statistics website offered by the experiment.  If no password is provided or the password is less than six characters in length, the website will be disabled. |
| `customRoutes` | `Function` | `lambda route: None` | Function that returns data to be returned when calling the Url `.../custom/<route>`

## Modes

The experiment can be run in three different modes, which are meant for different purposes.  For serving the website locally on a computer in a lab or similar, to then let an interviewee do the experiment on this computer, the mode `MODE.LOCAL` should be used.  This mode has the advantage that, even if the interviewee closes the browser and opens it again, the experiment will go on where it has been left.  Accordingly, one interviewee can do the experiment at a time, and the application needs to be quit and run again to perform another experiment.  All logs and results are saved with a timestamp but without any user identification.

When running the experiment with several interviewees at the same time, using several devices that are part of a local network or even the Web, either `MODE.USE_ACCESS_CODES` or `MODE.NO_ACCESS_CODES` should be used.  When running the experiment in the former mode, access codes are generated during the startup process, the number of which is defined by the parameter `numberOfAccessCodes` (default: 1000).  These codes are stored in the file `access-codes.csv` and need to be distributed to the interviewees.  By using such an access code, the interviewee can start his or her personal experiment.  Practically, this means that no interviewee can participate in two experiments unless he or she has two or more access codes.  The logs and results are stored with a reference to the access code.  The latter mode, `MODE.NO_ACCESS_CODES`, works in the same way, apart from generating access codes on the fly.  Interviewees do thus not need to enter any access code but can start with the experiment right away, which implies that they can, theoretically, participate in the experiment several times.

| Mode | Setting | Control over who is interviewed | Interviewees per Session | Access Codes | Logs and results |
| ---- | ------- | ------------------------------- | ------------------------ | ------------ | ---------------- |
| `MODE.LOCAL` | local | very high | 1 | – | `experiment-{ISO_DATE}.json` |
| `MODE.USE_ACCESS_CODES` | network | high | `numberOfAccessCodes` | need to be distributed to the interviewees | `experiment-{ACCESS_CODE}.json` |
| `MODE.NO_ACCESS_CODES` | network | low | practically infinite | generated on the fly | `experiment-{ACCESS_CODE}.json` |

To run the experiment with access codes, you would execute the following code:
```python
from Empiric import Experiment, MODE

def manuscript(m):
  ...

experiment = Experiment()
experiment.run(manuscript, mode=MODE.USE_ACCESS_CODES)
```

## Proxy Server

The experiment can be run online.  In this case, attention should be paid to privacy issues.  Please keep in mind that http connections are not secure, and a reverse proxy should be used to encrypt the connection using https.
