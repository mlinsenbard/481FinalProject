# MXPO
MXPO is a music suggestion knowledge engine. The engine will work by taking a user-entered song, artist, or album and generate suggestions for them based of many internal factors that are currently being determied. The finished product will be a [web UI hosted online](http://linsenbard.com/mxpo/).

# Setup
## Discogs API
To be able to work with the Discog API, we're going to be using their in-house python package. [View their Github repo](https://github.com/discogs/discogs_client) for installation instructions, but you should be able to do:

```sh
$ pip install discogs_client
```

## Pandas
To visualize and find relationships between the data we collect, we plan on using [Pandas](http://pandas.pydata.org/). Installation instructions are on their site.

# CMAP
The CMAP for this engine is included in the main folder of the repository. Feel free to make any edits to it using [CmapTools](http://cmap.ihmc.us/).
