# Logic Pro X automation scripts

## GetPluginsForTracks

This script gets all the instruments and effects used for every track of the currently open Logic Pro X project. Since the script relies on accessibility features, you must use the French or English one depending on your OS language.

### Example

![GetPluginsForTracks](https://github.com/leboeuf/logic-pro-x-automation/raw/master/screenshots/GetPluginsForTracks.png)

```
[
    {
        "trackInfo": {
            "instrumentName": "E-Piano",
            "audioEffects": [
                {
                    "isEnabled": 1,
                    "effectName": "Compressor"
                },
                {
                    "isEnabled": 0,
                    "effectName": "Chorus"
                },
                {
                    "isEnabled": 1,
                    "effectName": "Channel EQ"
                }
            ],
            "isEnabled": 1
        },
        "trackName": "Track 1 - Classic Electric Piano"
    },
    {
        "trackInfo": {
            "instrumentName": "RetroSyn",
            "audioEffects": [
                {
                    "isEnabled": 1,
                    "effectName": "Compressor"
                },
                {
                    "isEnabled": 0,
                    "effectName": "Channel EQ"
                },
                {
                    "isEnabled": 1,
                    "effectName": "Tape Delay"
                }
            ],
            "isEnabled": 1
        },
        "trackName": "Track 2 - Eighties Pop Bass"
    },
    {
        "trackInfo": {
            "instrumentName": "RetroSyn",
            "audioEffects": [
                {
                    "isEnabled": 1,
                    "effectName": "Compressor"
                },
                {
                    "isEnabled": 1,
                    "effectName": "Channel EQ"
                },
                {
                    "isEnabled": 1,
                    "effectName": "Ensemble"
                },
                {
                    "isEnabled": 1,
                    "effectName": "Phaser"
                },
                {
                    "isEnabled": 0,
                    "effectName": "Overdrive"
                },
                {
                    "isEnabled": 0,
                    "effectName": "St-Delay"
                },
                {
                    "isEnabled": 1,
                    "effectName": "Compressor"
                }
            ],
            "isEnabled": 1
        },
        "trackName": "Track 3- Gritty Lead"
    },
    {
        "trackInfo": {
            "instrumentName": "Vintage B3",
            "audioEffects": [
                {
                    "isEnabled": 1,
                    "effectName": "Compressor"
                }
            ],
            "isEnabled": 1
        },
        "trackName": "Track 4 - Classic Rock Organ"
    }
]
```