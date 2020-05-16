[back to readme](../../../)

# Collected Data

The data collected is stored in the path `collected-data`, which you will find in the root directory of your project.  For every interview or experiment made, one JSON file is created.  The name of such a file is either `experiment-{ISO_DATE}.json` or `experiment-{ACCESS_CODE}.json`, depending on the type of mode the experiment is run in (see the [Section about experiments](experiments.md)).  The structure of these files is, however, identical independent of the naming of the file.

There are two ways the collected data can be analysed.  First, `Empiric!` offers a website that offers statistical information and visualizations about the collected data.  More information on this can be found in the [Section about statistics](statistics.md).  Secondly, the data can also easily be accessed manually and analysed in more detail.  In order to do so, the structure of such a file is described in the following.

The general structure of each file looks like follows:
```json
{
  "metadata": {
    "accessCode": "..."
    "timestamp": "..."
  },
  "memory": {
    "1": {
      "typeOfPage": "Page???",
      "result": {
        "log": [],
        ...
      },
      "settings": {...},
      "statistics": {...}
    },
    "2": {...},
    "3": {...},
  }
}
```

The `metadata` section contains all information about the experiment performed by this one interviewee can be found.  This includes the access code used (in case, no access code is used, it displays `"_"`) and the timestamp of the point in time when the interviewee opened the page first.

The `memory` section contains the actual data collected.  For each page, registered information, or other type of step, a corresponding a sequential number is used as a key.  For each such step, a host of data is collected.  The key–value pair `typeOfPage` contains the type of the page or step run, which can be helpful when interpreting the `result` section.  This section contains information in the way the corresponding page has created it.  Usually, a `log` of all activities that the interviewee has performed on the page is included.  A section about the `settings` used to generate the page is included, which allows to trace what has been displayed to the interviewee, and a section `statistics` about the way the statistical information shall be prepared for the statistical analysis.
